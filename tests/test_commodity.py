import unittest
from app.models import Commodity
from app.services import commodity_service

class TestCommodity(unittest.TestCase):
    def setUp(self):
        # Create a new commodity
        self.commodity = commodity_service.add_commodity(
            name='Test Commodity',
            description='This is a test commodity.'
        )

    def test_get_all_commodities(self):
        # Test getting all commodities
        commodities = commodity_service.get_all_commodities()
        self.assertGreater(len(commodities), 0)

    def test_get_commodity_by_id(self):
        # Test getting a commodity by ID
        commodity = commodity_service.get_commodity_by_id(self.commodity.id)
        self.assertIsNotNone(commodity)
        self.assertEqual(commodity.name, 'Test Commodity')

    def test_update_commodity(self):
        # Test updating a commodity
        commodity = commodity_service.update_commodity(
            self.commodity.id,
            name='Updated Test Commodity',
            description='This is an updated test commodity.'
        )
        self.assertIsNotNone(commodity)
        self.assertEqual(commodity.name, 'Updated Test Commodity')
        self.assertEqual(commodity.description, 'This is an updated test commodity.')

    def test_delete_commodity(self):
        # Test deleting a commodity
        commodity_service.delete_commodity(self.commodity.id)
        commodity = commodity_service.get_commodity_by_id(self.commodity.id)
        self.assertIsNone(commodity)

if __name__ == '__main__':
    unittest.main()
