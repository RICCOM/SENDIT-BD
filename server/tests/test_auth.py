import unittest
from app import create_app, db
from models import User

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            self.create_user()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def create_user(self):
        user = User(username="testuser", email="test@example.com", password_hash="hashed_password")
        db.session.add(user)
        db.session.commit()

    def test_login(self):
        response = self.client.post('/login', json={'username': 'testuser', 'password': 'hashed_password'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.get_json())

    def test_register(self):
        response = self.client.post('/register', json={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

    def test_protected_route(self):
        login_response = self.client.post('/login', json={'username': 'testuser', 'password': 'hashed_password'})
        token = login_response.get_json().get('token')
        response = self.client.get('/protected', headers={'Authorization': token})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
