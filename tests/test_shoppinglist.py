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

    def test_remove_item_from_shoppinglist(self):
        self.shoppinglist.add_item(Item("4255", "Cabbages", 2000, 4))
        self.shoppinglist.add_item(Item("3902", "Carrots", 4000, 10))
        self.assertEqual(len(self.shoppinglist.items), 2,
                         "There must be two items in the list")
        self.shoppinglist.remove_item("3902")
        self.assertEqual(len(self.shoppinglist.items), 1,
                         "There must be one item left in the list")

        # test remove item from wrong shoppinglist
        clothes = ShoppingList("ab452", "Clothes", "2017-09-01")
        clothes.add_item(Item("46272", "Jeans", 15000, 3))
        self.assertEqual(len(clothes.items), 1, "One item in clothes")
        clothes.add_item(Item("3214", "Shirts", 30000, 3))
        self.assertEqual(len(clothes.items), 2, "Two item in clothes")
        self.shoppinglist.remove_item("3214")

    def test_get_item(self):
        clothes = ShoppingList("FE761", "Clothes", "2017-09-01")
        clothes.add_item(Item("5262Y", "Jeans", 15000, 3))
        self.assertEqual(len(clothes.items), 1, "One item in clothes")
        clothes.add_item(Item("HF671", "Shirts", 30000, 3))

        got_item = clothes.get_item("HF671")
        self.assertEqual(got_item.price, 30000,
                         "Price of an item must be 30000")
        self.assertEqual(got_item.quantity, 3, "Quantity must be 3")
        self.assertEqual(got_item.name, "Shirts", "Name must be Shirts")

        no_item = clothes.get_item("HDR71S")
        self.assertFalse(no_item, "No item available: supposed to return None")
