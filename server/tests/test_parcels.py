import unittest
from app import create_app, db
from models import Parcel

class ParcelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            self.create_parcel()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def create_parcel(self):
        parcel = Parcel(
            user_id=1,
            weight=10.5,
            pickup_address="123 Pickup St",
            pickup_lat=40.7128,
            pickup_lng=-74.0060,
            destination_address="456 Destination Ave",
            destination_lat=34.0522,
            destination_lng=-118.2437,
            status="Pending",
            present_location="Warehouse",
            present_location_lat=40.7128,
            present_location_lng=-74.0060
        )
        db.session.add(parcel)
        db.session.commit()

    def test_get_parcels(self):
        response = self.client.get('/parcels')
        self.assertEqual(response.status_code, 200)

    def test_get_parcel(self):
        response = self.client.get('/parcels/1')
        self.assertEqual(response.status_code, 200)

    def test_create_parcel(self):
        response = self.client.post('/parcels', json={
            'user_id': 1,
            'weight': 12.3,
            'pickup_address': '789 New Pickup St',
            'pickup_lat': 37.7749,
            'pickup_lng': -122.4194,
            'destination_address': '123 New Destination Ave',
            'destination_lat': 37.7749,
            'destination_lng': -122.4194,
            'status': 'In Transit',
            'present_location': 'In Transit',
            'present_location_lat': 37.7749,
            'present_location_lng': -122.4194
        })
        self.assertEqual(response.status_code, 201)

    def test_update_parcel(self):
        response = self.client.put('/parcels/1', json={'status': 'Delivered'})
        self.assertEqual(response.status_code, 200)

    def test_delete_parcel(self):
        response = self.client.delete('/parcels/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
