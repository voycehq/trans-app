from typing import Any, List, Optional
import google.cloud.texttospeech as tts

from app.dto.model.customer import CustomerDTO
from app.dto.model.language_setting import LanguageSettingDTO
from app.dto.model.text import TextDTO
from app.dto.model.translated_text import TranslatedTextDTO
from app.dto.model.workspace import WorkspaceDTO
from app.logs import logger
from app.service.model.customer import CustomerLib
from app.service.model.language_setting import LanguageSettingLib
from app.service.model.text import TextLib
from app.service.model.translated_text import TranslatedTextLib
from app.service.model.workspace import WorkspaceLib
from config import base_dir

class AudioGenerator:
    """
    This class is responsible for generating audio files
    for registered translated scripts from original an original text
    """
    
    def __init__(self, workspace_id: int, raw_text_id: int) -> None:
        self.workspace_id: int = workspace_id
        self.raw_text_id = raw_text_id
        
        # ** Constants
        self.__BASE_DIR = f'{base_dir}/static/customer/audios'
        self.__customer: Optional[CustomerDTO] = None
        self.__workspace: Optional[WorkspaceDTO] = None
        self.__raw_text: Optional[TextDTO] = None
        self.__translated_scripts: List[TranslatedTextDTO] = []
        
        # ** After init
        self.__after_init__()
    
    @property
    def raw_text(self):
        raw_text_object: Optional[TextDTO] = TextLib.find_by(where={'id': self.raw_text_id})
        self.__raw_text = raw_text_object
        return self.__raw_text
    
    @property
    def workspace(self):
        workspace_object: Optional[WorkspaceDTO] = WorkspaceLib.find_by(where={'id': self.workspace_id})
        
        if workspace_object:
            self.__workspace = workspace_object
            
            # Get the cusotmer
            customer_object: Optional[CustomerDTO] = CustomerLib.find_by(where={'id': workspace_object.customer_id})
            self.__customer = customer_object
        else:
            self.__workspace = None
            self.__customer = None

        return self.__workspace
    
    @property
    def translated_scripts(self):
        translated_script_objects: List[TranslatedTextDTO] = TranslatedTextLib.get_all_by_text_id(text_id=self.raw_text_id)
        self.__translated_scripts = translated_script_objects
        return self.__translated_scripts
    
    def __after_init__(self):
        # ** 1st: Validate workspace
        if not self.__workspace or self.__workspace is None:
            raise Exception(f'Workspace with workspace_id={self.workspace_id} is not found.')
        
        # ** 1st: Validate text if it exists
        if not self.__raw_text or self.__raw_text is None:
            raise Exception('Original script not found')
        
        # ** 1st: Validate translation scripts are available
        if not self.__translated_scripts or self.__translated_scripts:
            raise Exception('No translated script found')
    
    def __resolve_customer_folder__(self) -> str:
        """This function will resolve the customer folder name

        Returns:
            str: The name of the customer folder
        """
        import os

        folder_path = f'{self.__BASE_DIR}/{self.__customer.id}{self.workspace.id}'
        os.makedirs(folder_path, exist_ok=True)
        
        return folder_path
    
    def __resolve_audio_filename__(self, target_language_code: str) -> str:
        """This function will resolve the generated audio filename

        Returns:
            str: The name of the generated audio file
        """
        from datetime import datetime
        import math
        
        return f'{target_language_code}-{math.ceil(datetime.timestamp(datetime.now()))}.mp3'
    
    def __save_audio_file__(self, filename: str, tts_response: Any) -> None:
        from pathlib import Path
        
        # * Ensure customer audio folder is existing
        folder_path = self.__resolve_customer_folder__()
        
        # * Save audio file
        filepath = f'{folder_path}/{filename}'
        audio_file = Path(f'{filepath}')
        audio_file.touch(exist_ok=True)
        
        with open(filepath, "wb") as file:
            file.write(tts_response.audio_content)
        
        logger.info(f'Done saving audio file.')
        
        return
    
    @staticmethod
    def __unique_languages_from_voices__(voices):
        language_set = set()
        for voice in voices:
            for language_code in voice.language_codes:
                language_set.add(language_code)
        return language_set
    
    @staticmethod
    def list_languages() -> list:
        client = tts.TextToSpeechClient()
        response = client.list_voices()
        languages = AudioGenerator.__unique_languages_from_voices__(response.voices)

        logger.info(f" Languages: {len(languages)} ".center(60, "-"))
        for i, language in enumerate(sorted(languages)):
            logger.info(f"{language:>10}", end="\n" if i % 5 == 4 else "")
        
        return languages
    
    @staticmethod
    def list_voices(language_code=None) -> list:
        client = tts.TextToSpeechClient()
        response = client.list_voices(language_code=language_code)
        voices = sorted(response.voices, key=lambda voice: voice.name)

        logger.info(f" Voices: {len(voices)} ".center(60, "-"))
        for voice in voices:
            languages = ", ".join(voice.language_codes)
            name = voice.name
            gender = tts.SsmlVoiceGender(voice.ssml_gender).name
            rate = voice.natural_sample_rate_hertz
            logger.info(f"{languages:<8} | {name:<24} | {gender:<8} | {rate:,} Hz")
        
        return voices
    
    def generate(self) -> None:
        """
        This is the main generator function that generates the audio (MP3)
        for the translated script text.
        """
        from datetime import datetime    

        logger.info('Start generating audio files for translated scripts')
        # ** Loop through the translated text to generate audio
        for script in self.translated_scripts:
            # ** Ensure script has been reviewed
            if not script.reviewed_by or script.reviewed_by is None:
                logger.warn(f'The script with translated_text_id={script.id} has not yet being reviewed.')
                continue
            
            # * 1st: Get language setting
            language_setting: Optional[LanguageSettingDTO] = LanguageSettingLib.find_by(where={'language_id': script.language_id})
            
            if not language_setting:
                logger.warn(f'No language setting found for language_id={script.language_id}')
            
            # * 2nd: Synthesis text
            synthesize_script = tts.SynthesisInput(text=script.body)
            
            # * 3rd: Setup voice params
            voice_params = tts.VoiceSelectionParams(
                language_code=language_setting.voice_language_code,
                name=language_setting.voice_name
            )
            
            # * 4th: Setup audio configurations
            audio_config = tts.AudioConfig(
                audio_encoding=language_setting.audio_encoding,
                speaking_rate=language_setting.audio_speaking_rate,
                pitch=language_setting.audio_pitch
            )
            
            # * 5th: Get audio generator client
            client = tts.TextToSpeechClient()

            # * 6th: Get the response
            response = client.synthesize_speech(
                input=synthesize_script, voice=voice_params, audio_config=audio_config
            )
            
            # * 7th: Get filename
            audio_filename: str = self.__resolve_audio_filename__(target_language_code=language_setting.voice_language_code)
            
            # * 8th: Save audio file
            self.__save_audio_file__(filename=audio_filename, tts_response=response)
            
            logger.info(f'Successfully generated audio for language_code={language_setting.voice_language_code}')
            
            # * 9th: Update TranslatedText object
            TranslatedTextLib.update(data={'text_id': script.text_id, 'language_id': script.language_id, 'audio_generation_date': datetime.now() })

        logger.info('Done generating audio files for translated scripts')
        return
