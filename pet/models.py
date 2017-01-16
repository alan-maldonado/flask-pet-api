from application import db

from store.models import Store

class Pet(db.Document):
    external_id = db.StringField(db_field="external_id")
    name = db.StringField(db_field="name")
    species = db.StringField(db_field="species")
    breed = db.StringField(db_field="breed")
    age = db.IntField(db_field="age")
    store = db.ReferenceField(Store, db_field="store")
    price = db.DecimalField(db_field="price", precision=2, rounding='ROUND_HALF_UP')
    sold = db.BooleanField(db_field="sold", default=False)
    received_date = db.DateTimeField(db_field="received_date")
    sold_date = db.DateTimeField(db_field="sold_date")
    live = db.BooleanField(db_field="live", default=True)

    meta = {
        'indexes': [('external_id', 'live'), ('species', 'breed', 'live'), ('store', 'live')]
    }
