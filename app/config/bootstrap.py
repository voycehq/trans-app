class Bootstrap:
    def __init__(self):
        pass

    def run(self):
        self.populate_date_model()
        self.populate_workspace_roles()
        self.populate_languages()

    def populate_date_model(self):
        from app.service.model.date import DateLib

        DateLib().run()

    def populate_workspace_roles(self):
        from app.service.model.workspace_role import WorkspaceRoleLib
        from app.logs import logger

        roles = ["admin", "reviewer"]
        WorkspaceRoleLib.bulk_create(names=roles)

        logger.info(f"Done Creating customer roles")

    def populate_languages(self):
        from app.service.model.language import LanguageLib
        from app.logs import logger

        languages = [{'name': 'English', 'code': 'en', 'html_code': 'translator-lang-option-en-US'},
                     {'name': 'French', 'code': 'fr', 'html_code': 'translator-lang-option-fr-FR'},
                     {'name': 'Spanish', 'code': 'es', 'html_code': 'translator-lang-option-es-ES'}]

        LanguageLib.bulk_create(records=languages)

        logger.info(f"Done Creating customer Languages")