from run import current_app
from database import db
from config import TestConfigurarion
from flask_testing import TestCase

class BaseTestCase(TestCase):

    def create_app(self):
        app = current_app()
        app.config.from_object(TestConfigurarion)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()