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

        languages = [{'name': 'English', 'code': 'en', 'html_code': "translator-lang-option-en-US"},
                     {'name': 'French', 'code': 'fr', 'html_code': 'translator-lang-option-fr-FR'},
                     {'name': 'Spanish', 'code': 'es', 'html_code': 'translator-lang-option-es-ES'}]

        LanguageLib.bulk_create(records=languages)

        logger.info(f"Done Creating Languages")

    def populate_language_settings(self):
        from app.service.model.language_setting import LanguageSettingLib
        from app.logs import logger

        language_settings = [{'name': 'French',
                                'voice_language_name': 'French(France)',
                                'voice_language_code': 'fr-FR',
                                'voice_name': 'fr-FR-Wavenet-D',
                                'audio_encoding': 1,
                                'audio_pitch': 1,
                                'audio_speaking_rate': 0
                            }, {'name': 'Spanish',
                                'voice_language_name': 'Spanish',
                                'voice_language_code': 'es-ES',
                                'voice_gender': 'female',
                                'voice_name': 'es-ES-Wavenet-C',
                                'audio_encoding': 1,
                                'audio_pitch': 1.6,
                                'audio_speaking_rate': 0
                            },{'name': 'English',
                                'voice_language_name': 'English(United States)',
                                'voice_language_code': 'es-US',
                                'voice_name': 'en-US-Wavenet-G',
                                'audio_encoding': 1,
                                'audio_pitch': 0,
                                'audio_speaking_rate': 0.9
                            }]

        LanguageSettingLib.bulk_create(records=language_settings)
        logger.info(f"Done Creating Language Settings")
