import unittest

from datetime import datetime
from models.shoppinglist import ShoppingList
from models.item import Item


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shoppinglist = ShoppingList("3572", "Groceries", "2017-08-04")

    def test_add_item(self):
        length = len(self.shoppinglist.items)
        self.shoppinglist.add_item(Item("12345", "Cabbages", 2000, 4))
        self.assertEqual(len(self.shoppinglist.items), 1,
                         "The shopping list has just one item")
        self.assertEqual(len(self.shoppinglist.items), length + 1,
                         "The number has just been incremented by one")
        self.assertEqual(self.shoppinglist.date_modified,
                         datetime.now().strftime("%Y-%m-%d %H:%M"))
