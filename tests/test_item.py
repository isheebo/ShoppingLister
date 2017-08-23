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
