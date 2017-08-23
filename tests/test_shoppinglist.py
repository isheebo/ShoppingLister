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

    def test_add_duplicate_item_to_shopping_list(self):
        self.shoppinglist.add_item(Item("1243", "Cabbages", 2000, 4))
        self.assertFalse(self.shoppinglist.add_item(
            Item("1243", "Cabbages", 3000, 5)), "Duplicate items not allowed")
        self.assertEqual(len(self.shoppinglist.items), 1,
                         "The shopping list has just one item")
        self.shoppinglist.add_item(Item("4553", "Carrots", 4000, 10))
        self.assertEqual(len(self.shoppinglist.items), 2,
                         "The items in the list must now be two")
