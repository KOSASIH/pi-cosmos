# Test the Commodity model and service
import unittest
from app.models import Commodity
from app.services import commodity_service

class TestCommodity(unittest.TestCase):
    def test_get_all_commodities(self):
        commodities = commodity_service.get_all_commodities()
        self.assertGreater(len(commodities), 0)
