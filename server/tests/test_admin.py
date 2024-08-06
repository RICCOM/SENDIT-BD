import unittest
from app import create_app, db
from models import Admin

class AdminTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            self.create_admin()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def create_admin(self):
        admin = Admin(username="admin", email="admin@example.com", password_hash="hashed_password")
        db.session.add(admin)
        db.session.commit()

    def test_get_admin(self):
        response = self.client.get('/admins/1')
        self.assertEqual(response.status_code, 200)

    def test_create_admin(self):
        response = self.client.post('/admins', json={
            'username': 'new_admin',
            'email': 'new_admin@example.com',
            'password_hash': 'hashed_password'
        })
        self.assertEqual(response.status_code, 201)

    def test_update_admin(self):
        response = self.client.put('/admins/1', json={'email': 'new_email@example.com'})
        self.assertEqual(response.status_code, 200)

    def test_delete_admin(self):
        response = self.client.delete('/admins/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
