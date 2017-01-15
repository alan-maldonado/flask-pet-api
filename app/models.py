from application import db

class App(db.Document):
    app_id = db.StringField(db_field="app_id", unique=True)
    app_secret = db.StringField(db_field="app_secret")

    meta = {
        'indexes': [('app_id')]
    }

class Access(db.Document):
    app = db.ReferenceField(App, db_field="app")
    token = db.StringField(db_field="token")
    expires = db.DateTimeField(db_field="expires")
