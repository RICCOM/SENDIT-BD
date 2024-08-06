import unittest
from app import create_app, db

class InitTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_app_initialization(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)  # Assuming no route for '/' in the app

if __name__ == '__main__':
    unittest.main()
