class Bootstrap:
    def __init__(self):
        pass

    def run(self):
        import os
        from config import base_dir
        
        # * Seed DB
        self.populate_date_model()
        self.populate_workspace_roles()
        self.populate_languages()
        self.populate_language_settings()
        
        # * Setup system environment for Google TTS
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f'{base_dir}/voyce-google-tts-credentials.json'

    def populate_date_model(self):
        from app.service.model.date import DateLib

        DateLib().run()

    def populate_workspace_roles(self):
        from app.service.model.workspace_role import WorkspaceRoleLib
        from app.logs import logger

        roles = [{"name": "admin"}, {"name": "reviewer"}]
        WorkspaceRoleLib.bulk_create(names=roles)

        logger.info(f"Done Creating workspace roles")

    def populate_languages(self):
        from app.service.model.language import LanguageLib
        from app.logs import logger

        languages = [{'name': 'English (American)', 'code': 'en-US', 'html_code': "translator-lang-option-en-US"},
                     {'name': 'English (British)', 'code': 'en-GB', 'html_code': 'translator-lang-option-en-GB'},
                     {'name': 'French', 'code': 'fr-FR', 'html_code': 'translator-lang-option-fr-FR'},
                     {'name': 'Romanian', 'code': 'ro-RO', 'html_code': 'translator-lang-option-ro-RO'},
                     {'name': 'Italian', 'code': 'it-IT', 'html_code': 'translator-lang-option-it-IT'},
                     {'name': 'Portuguese (Brazilian)', 'code': 'pt-BR', 'html_code': 'translator-lang-option-pt-BR'},
                     {'name': 'Portuguese (Portugal)', 'code': 'pt-PT', 'html_code': 'translator-lang-option-pt-PT'},
                     {'name': 'German', 'code': 'de-DE', 'html_code': 'translator-lang-option-de-DE'},
                     {'name': 'Chinese (simplified)', 'code': 'zh-ZH', 'html_code': 'translator-lang-option-zh-ZH'},
                     {'name': 'Japanese', 'code': 'ja-JA', 'html_code': 'translator-lang-option-ja-JA'},
                     {'name': 'Russian', 'code': 'ru-RU', 'html_code': 'translator-lang-option-ru-RU'},
                     {'name': 'Polish', 'code': 'pl-PL', 'html_code': 'translator-lang-option-pl-PL'},
                     {'name': 'Slovak', 'code': 'sk-SK', 'html_code': 'translator-lang-option-sk-SK'},
                     {'name': 'Spanish', 'code': 'es-ES', 'html_code': 'translator-lang-option-es-ES'}]

        LanguageLib.bulk_create(records=languages)

        logger.info(f"Done Creating Languages")

    def populate_language_settings(self):
        from app.service.model.language_setting import LanguageSettingLib
        from app.logs import logger

        language_settings = [
            {
                'name': 'French',
                'voice_language_name': 'French(France)',
                'voice_language_code': 'fr-FR',
                'voice_name': 'fr-FR-Wavenet-D',
                'audio_encoding': 1,
                'audio_pitch': 1,
                'audio_speaking_rate': 0
            }, 
            {
                'name': 'Spanish',
                'voice_language_name': 'Spanish',
                'voice_language_code': 'es-ES',
                'voice_gender': 'female',
                'voice_name': 'es-ES-Wavenet-C',
                'audio_encoding': 1,
                'audio_pitch': 1.6,
                'audio_speaking_rate': 0
            },
            {
                'name': 'English',
                'voice_language_name': 'English(United States)',
                'voice_language_code': 'es-US',
                'voice_name': 'en-US-Wavenet-G',
                'audio_encoding': 1,
                'audio_pitch': 0,
                'audio_speaking_rate': 0.9
            },
            {
                'name': 'English',
                'voice_language_name': 'English (UK)',
                'voice_language_code': 'es-GB',
                'voice_name': 'en-GB-Wavenet-D',
                'audio_encoding': 1,
                'audio_pitch': 0,
                'audio_speaking_rate': 0.93
            },
            {
                'name': 'Romanian',
                'voice_language_name': 'Romanian (Romania)',
                'voice_language_code': 'ro-RO',
                'voice_name': 'ro-RO-Wavenet-A',
                'audio_encoding': 1,
                'audio_pitch': 0,
                'audio_speaking_rate': 0.93
            },
            {
                'name': 'Italian',
                'voice_language_name': 'Italian (Italy)',
                'voice_language_code': 'it-IT',
                'voice_name': 'it-IT-Wavenet-C',
                'audio_encoding': 1,
                'audio_pitch': 0,
                'audio_speaking_rate': 0.85
            },
            {
                'name': 'Portuguese (Brazil)',
                'voice_language_name': 'Portuguese (Brazil)',
                'voice_language_code': 'pt-BR',
                'voice_name': 'pt-BR-Wavenet-B',
                'audio_encoding': 1,
                'audio_pitch': 0,
                'audio_speaking_rate': 0.93
            },
            {
                'name': 'German',
                'voice_language_name': 'German (Germany)',
                'voice_language_code': 'de-DE',
                'voice_name': 'de-DE-Wavenet-F',
                'audio_encoding': 1,
                'audio_pitch': 0,
                'audio_speaking_rate': 0.93
            },
            {
                'name': 'Japanese',
                'voice_language_name': 'Japanese (Japan)',
                'voice_language_code': 'ja-JP',
                'voice_name': 'ja-JP-Wavenet-D',
                'audio_encoding': 1,
                'audio_pitch': 0,
                'audio_speaking_rate': 0.93
            },
            {
                'name': 'Chinese',
                'voice_language_name': 'Mandarin Chinese',
                'voice_language_code': 'cmn-CN',
                'voice_name': 'cmn-CN-Wavenet-A',
                'audio_encoding': 1,
                'audio_pitch': 0,
                'audio_speaking_rate': 0.93
            },
            {
                'name': 'Russian',
                'voice_language_name': 'Russian (Russia)',
                'voice_language_code': 'ru-RU',
                'voice_name': 'ru-RU-Wavenet-B',
                'audio_encoding': 1,
                'audio_pitch': 0,
                'audio_speaking_rate': 0.93
            },
            {
                'name': 'Polish',
                'voice_language_name': 'Polish (Poland)',
                'voice_language_code': 'pl-PL',
                'voice_name': 'pl-PL-Wavenet-C',
                'audio_encoding': 1,
                'audio_pitch': 0,
                'audio_speaking_rate': 0.93
            },
            {
                'name': 'Slovak',
                'voice_language_name': 'Slovak (Slovakia)',
                'voice_language_code': 'sk-SK',
                'voice_name': 'sk-SK-Wavenet-A',
                'audio_encoding': 1,
                'audio_pitch': 0,
                'audio_speaking_rate': 0.93
            },
        ]

        LanguageSettingLib.bulk_create(records=language_settings)
        logger.info(f"Done Creating Language Settings")
