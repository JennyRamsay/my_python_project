import unittest
from models.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jennifer", "Premium")

    def test_customer_has_name(self):
        self.assertEqual("Jennifer", self.customer.full_name)

    def test_customer_has_customership(self):
        self.assertEqual("Premium", self.customer.customership)