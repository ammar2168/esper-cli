from tinydb import Query


class DBWrapper:

    def __init__(self, db):
        self.db = db

    def set_configure(self, configure_data):
        Configure = Query()

        if self.db.get(Configure.config.exists()):
            self.db.remove(Configure.config.exists())

        self.db.insert({'config': configure_data})

    def get_configure(self):
        Configure = Query()

        db_result = self.db.get(Configure.config.exists())

        configure = None
        if db_result:
            configure = db_result['config']

        return configure

    def get_enterprise_id(self):
        configure = self.get_configure()
        return configure.get('enterprise_id') if configure else None

    def set_application(self, application):
        Application = Query()

        if self.db.get(Application.application.exists()):
            self.db.remove(Application.application.exists())

        self.db.insert({'application': application})

    def get_application(self):
        Application = Query()

        db_result = self.db.get(Application.application.exists())

        application = None
        if db_result:
            application = db_result['application']

        return application

    def unset_application(self):
        Application = Query()
        self.db.remove(Application.application.exists())