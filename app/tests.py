from application import create_app as create_app_base
from mongoengine.connection import _get_db
import unittest
import json
from datetime import datetime, timedelta

from app.models import App, Access
from settings import MONGODB_HOST

class AppTest(unittest.TestCase):
    def create_app(self):
        self.db_name = 'pets-api-test'
        return create_app_base(
            MONGODB_SETTINGS={'DB': self.db_name,
                'HOST': MONGODB_HOST},
            TESTING=True,
            WTF_CSRF_ENABLED=False,
            SECRET_KEY = 'mySecret!',
        )

    def setUp(self):
        self.app_factory = self.create_app()
        self.app = self.app_factory.test_client()

    def tearDown(self):
        db = _get_db()
        db.client.drop_database(db)

    def app_dict(self):
        return json.dumps(dict(
                app_id="pet_client",
                app_secret="pet_secret"
                ))

    def test_create_app(self):
        # basic registration
        rv = self.app.post('/apps/',
            data=self.app_dict(),
            content_type='application/json')
        assert rv.status_code == 200

        # missing app_secret
        missing_app_dict = json.dumps(dict(
                app_id="pet_client"
                ))
        rv = self.app.post('/apps/',
            data=missing_app_dict,
            content_type='application/json')
        assert "MISSING_APP_ID_OR_APP_SECRET" in str(rv.data)

        # repeat registration
        rv = self.app.post('/apps/',
            data=self.app_dict(),
            content_type='application/json')
        assert "APP_ID_ALREADY_EXISTS" in str(rv.data)
