import unittest
from app import create_app, db
from models import Notification

class NotificationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            self.create_notification()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def create_notification(self):
        notification = Notification(user_id=1, parcel_id=1, message="Test notification")
        db.session.add(notification)
        db.session.commit()

    def test_get_notifications(self):
        response = self.client.get('/notifications')
        self.assertEqual(response.status_code, 200)

    def test_get_notification(self):
        response = self.client.get('/notifications/1')
        self.assertEqual(response.status_code, 200)

    def test_create_notification(self):
        response = self.client.post('/notifications', json={
            'user_id': 1,
            'parcel_id': 1,
            'message': 'New notification'
        })
        self.assertEqual(response.status_code, 201)

    def test_update_notification(self):
        response = self.client.put('/notifications/1', json={'message': 'Updated message'})
        self.assertEqual(response.status_code, 200)

    def test_delete_notification(self):
        response = self.client.delete('/notifications/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
