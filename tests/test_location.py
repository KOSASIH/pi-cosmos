import unittest
from app.models import Location
from app.services import location_service

class TestLocation(unittest.TestCase):
    def setUp(self):
        # Create a new location
        self.location = location_service.add_location(
            name='Test Location',
            address='123 Test St',
            city='Test City',
            state='Test State',
            zip_code='12345'
        )

    def test_get_all_locations(self):
        # Test getting all locations
        locations = location_service.get_all_locations()
        self.assertGreater(len(locations), 0)

    def test_get_location_by_id(self):
        # Test getting a location by ID
        location = location_service.get_location_by_id(self.location.id)
        self.assertIsNotNone(location)
        self.assertEqual(location.name, 'Test Location')

    def test_update_location(self):
        # Test updating a location
        location = location_service.update_location(
            self.location.id,
            name='Updated Test Location',
            address='456 Test St',
            city='Updated Test City',
            state='Updated Test State',
            zip_code='67890'
        )
        self.assertIsNotNone(location)
        self.assertEqual(location.name, 'Updated Test Location')
        self.assertEqual(location.address, '456 Test St')
        self.assertEqual(location.city, 'Updated Test City')
        self.assertEqual(location.state, 'Updated Test State')
        self.assertEqual(location.zip_code, '67890')

    def test_delete_location(self):
        # Test deleting a location
        location_service.delete_location(self.location.id)
        location = location_service.get_location_by_id(self.location.id)
        self.assertIsNone(location)

if __name__ == '__main__':
    unittest.main()
