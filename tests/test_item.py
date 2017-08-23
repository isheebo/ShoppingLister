import unittest
from models.item import Item


class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item("1345", "Cabbages", 200, 4)

    def test_item_id(self):
        self.assertEqual(self.item.item_id, "1345", "item ID must be 1345")

    def test_name_of_item(self):
        self.assertEqual(self.item.name, "Cabbages",
                         "name of the item must be Cabbages.")
        self.item.name = "Carrots"
        self.assertEqual(self.item.name, "Carrots",
                         "name of the item has now changed to Carrots")

    def test_price_of_item(self):
        self.assertEqual(self.item.price, 200, "Price must be 200")
        self.item.price = 120
        self.assertEqual(self.item.price, 120, "Price must now be 120")

    def test_quantity_of_item(self):
        self.assertEqual(self.item.quantity, 4, "Quantity must be 4")
        self.item.quantity = 6
        self.assertEqual(self.item.quantity, 6, "Quantity must now be 6")
