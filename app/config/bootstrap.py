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

        WorkspaceRoleLib().run()

    def populate_languages(self):
        from app.service.model.language import LanguageLib

        LanguageLib().run()
