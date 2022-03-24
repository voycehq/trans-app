from pyvirtualdisplay import Display

from typing import Any, Dict, List, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By

from app.logs import logger
from app.dto.model.language import LanguageDTO
from app.dto.model.text import TextDTO
from app.dto.model.translated_text import TranslatedTextDTO
from app.service.model.language import LanguageLib
from app.service.model.text import TextLib
from app.service.model.translated_text import TranslatedTextLib
from config import base_dir
from config import config


class Translator:
    """
    This class is an automated script that receives an english script
    and returns the translated script in the specified target_lang_code.
    Currently we support only 'fr' -- 'French' and 'es' -- 'Spanish'
    """

    def __init__(self, text_id: int, language_ids: List[int]) -> None:
        self.text_id: str = text_id
        self.language_ids: List[int] = language_ids

        # * Constants
        self.__raw_text: Optional[TextDTO] = None
        self.__languages: List[LanguageDTO] = []

        # * Run after init function for validations
        self.__after_init__()

    @property
    def raw_text(self):
        logger.info('Fetching original text from DB')
        raw_text_object: Optional[TextDTO] = TextLib.find_by(where={'id': self.text_id})
        self.__raw_text = raw_text_object if raw_text_object else None
        return self.__raw_text

    @property
    def languages(self):
        logger.info('Fetching target language objects from DB')
        language_objects = []

        for language_id in self.language_ids:
            language = LanguageLib.find_by(where={'id': language_id})

            if language:
                language_objects.append(language)

        self.__languages = language_objects
        return self.__languages

    def __after_init__(self) -> None:
        """
        This function validates the various inputted params
        """
        # * validate original script
        self.__validate_original_text__()

        # * validate target translation languages
        self.__validate_target_languages__()

        return

    def __validate_original_text__(self) -> None:
        # ** 1st: validate to ensure that length is not > 5000 characters
        if (len(self.raw_text.body) > 5000):
            raise Exception('Original script length should not excede 5000 characters')

    def __validate_target_languages__(self) -> None:
        # ** 1st: Ensure that we have are target translation languages loaded from the DB
        if not self.languages:
            raise Exception('None of desired target languages for transalation are supported yet.')

    def __configure_chrome_driver__(self) -> webdriver:
        from pyvirtualdisplay import Display
        from selenium import webdriver

        display = Display(visible=0, size=(800, 600))
        display.start()

        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument("--headless")
        options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(chrome_options=options)
        return driver

    def __select_target_language__(self, targetSectionPanel: Any, target_language_id: int) -> None:
        from selenium.common.exceptions import ElementClickInterceptedException

        # ** Drop down menu to select target language
        targetSectionPanel.find_element(by=By.XPATH, value="//button[@dl-test='translator-target-lang-btn']").click()

        try:
            # * Get target translation language object
            language: LanguageDTO = list(filter(lambda language: language.id == target_language_id, self.languages))[0]

            target_language_html_code = language.html_code
            targetSectionPanel.find_element(by=By.CSS_SELECTOR, value='.lmt__textarea_container').find_element(
                by=By.XPATH, value=f"//div[@dl-test='translator-target-lang-list']").find_element(
                by=By.XPATH, value="//button[@dl-test='{id}']".format(id=target_language_html_code)).click()

        except IndexError:
            raise Exception('Target language ID is incorrect.')

        except ElementClickInterceptedException:
            logger.info('RETRYING SELECTOR PICKER >>>>>>>>')
            targetSectionPanel.find_element(by=By.CSS_SELECTOR, value='.lmt__textarea_container').find_element(
                by=By.XPATH, value=f"//div[@dl-test='translator-target-lang-list']").find_element(
                by=By.XPATH, value="//button[@dl-test='{id}']".format(id=target_language_html_code)).click()

    def __inject_raw_script_for_translation__(self, driver: webdriver) -> None:
        # ** Input raw text to be translated
        driver.find_element(by=By.ID, value='panelTranslateText').find_element(by=By.XPATH,
                                                                               value="//textarea[@dl-test='translator-source-input']").send_keys(
            f"""{self.raw_text.body}""")

    def __translate_script__(self, target_language: LanguageDTO) -> Optional[Dict[str, Any]]:
        import datetime, time

        try:
            # ** Configure selenium Chrome driver
            logger.info('Configuring webdriver for web scrapping')
            driver = self.__configure_chrome_driver__()
            driver.get(config.TRANSLATOR_URL)

            # ** Get root containers
            logger.info(f'Start script translation for target_laguage_code={target_language.code}')
            translationPanel = driver.find_element(by=By.ID, value='panelTranslateText')
            sourceSectionPanel = translationPanel.find_element(by=By.XPATH,
                                                               value="//section[@dl-test='translator-source']")
            targetSectionPanel = translationPanel.find_element(by=By.XPATH,
                                                               value="//section[@dl-test='translator-target']")

            # ** Select target language
            self.__select_target_language__(targetSectionPanel=targetSectionPanel,
                                            target_language_id=target_language.id)

            # ** Input raw text for translation
            self.__inject_raw_script_for_translation__(driver=driver)

            # ** Get translated script once it's ready
            translatedScript = ''
            while len(translatedScript.strip()) == 0:
                translatedScript = targetSectionPanel.find_element(by=By.ID, value='target-dummydiv').get_attribute(
                    'innerHTML')
            else:
                logger.info(f'Done with script translation with target_language_code={target_language.code}')

                # ** Build response
                response_body = {
                    'text_id': self.raw_text.id,
                    'language_id': target_language.id,
                    'body': translatedScript,
                    'translated_date': datetime.datetime.now(),
                }

                return response_body
        except Exception as e:
            logger.error(f'Error occured when translating script with target_lang_code={target_language.code}: {e}')
            logger.error('This can be due to poor internet connection.')
            return None

    def translate(self) -> List[TranslatedTextDTO]:
        try:
            translatedScripts: List[TranslatedTextDTO] = []

            # ** Loop through the various target languages and translate script
            for language in self.languages:
                # * 1st: Translate script
                translatedScript: Optional[Dict[str, Any]] = self.__translate_script__(target_language=language)

                # * 2nd: Append translated script
                if translatedScript: translatedScripts.append(translatedScript)

            # ** Bulk save the transalated scripts
            TranslatedTextLib.bulk_save(payload=translatedScripts)

            # ** Fetch all translated scripts for the given text
            response = TranslatedTextLib.get_all_by_text_id(text_id=self.raw_text.id)

            # ** Return response
            return response
        except Exception as e:
            logger.error(f'Error occured when translating script with target_language_ids={self.language_ids}: {e}')
            logger.error('This can be due to poor internet connection.')
            return []
