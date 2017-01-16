from mongoengine import signals
from application import db

class Store(db.Document):
    external_id = db.StringField(db_field="external_id")
    neighborhood = db.StringField(db_field="neighborhood")
    street_address = db.StringField(db_field="street_address")
    city = db.StringField(db_field="city")
    state = db.StringField(db_field="state")
    zip = db.StringField(db_field="zip")
    phone = db.StringField(db_field="phone")
    live = db.BooleanField(db_field="live", default=True)

    meta = {
        'indexes': [('external_id', 'live')]
    }
