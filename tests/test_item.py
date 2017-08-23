import unittest
from models.item import Item


class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item("1345", "Cabbages", 200, 4)

    def test_item_id(self):
        self.assertEqual(self.item.item_id, "1345", "item ID must be 1345")
