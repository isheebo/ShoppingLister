import unittest
from shoppinglister.models.user import User
from shoppinglister.models.shoppinglist import ShoppingList


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Kanyesigye Edgar", "kedgar751@gmail.com", "password")

    def test_create_user(self):
        self.assertTrue(self.user)
        self.assertEqual(self.user.name, "Kanyesigye Edgar",
                         "Name must be Kanyesigye Edgar")
        self.assertEqual(self.user.email, "kedgar751@gmail.com",
                         "Email must be kedgar751@gmail.com")
        self.assertEqual(len(self.user.shoppinglists), 0,
                         "Length of shopping lists must be 0")

    def test_user_create_shopping_list(self):
        self.assertEqual(len(self.user.shoppinglists), 0,
                         "No shopping lists created for this user yet")
        self.user.create_shoppinglist(ShoppingList(
            "HSTU728", "Vegetables", "2017-08-27"))
        self.assertEqual(
            self.user.shoppinglists["HSTU728"].notify_date, "2017-08-27",
            "date must be 2017-08-27")
        self.assertEqual(len(self.user.shoppinglists), 1,
                         "One item created on the user profile")

    def test_user_delete_shopping_list(self):
        self.assertEqual(len(self.user.shoppinglists), 0,
                         "Length must be zero. No items added.Yet!")
        self.user.create_shoppinglist(ShoppingList(
            "HS86HF", "Vegetables", "2017-08-27"))
        self.assertEqual(len(self.user.shoppinglists), 1,
                         "One shopping list added on user account")
        self.assertTrue(self.user.delete_shoppinglist("HS86HF"))
        self.assertEqual(len(self.user.shoppinglists), 0,
                         "Length must be zero. The item has been deleted")

    def test_edit_shopping_list(self):
        self.user.create_shoppinglist(ShoppingList(
            "HKUA452SA", "Vegetables", "2017-08-27"))
        self.assertEqual(self.user.shoppinglists["HKUA452SA"].name,
                         "Vegetables",
                         "Name of shopping list must be Vegetables")
        self.assertEqual(
            self.user.shoppinglists["HKUA452SA"].notify_date, "2017-08-27")

        self.assertTrue(self.user.edit_shoppinglist(
            "HKUA452SA", "Groceries", "2018-01-01"))
        self.assertEqual(
            self.user.shoppinglists["HKUA452SA"].name, "Groceries")
        self.assertEqual(
            self.user.shoppinglists["HKUA452SA"].notify_date, "2018-01-01")

        self.user.edit_shoppinglist("HKUA452SA", "Clothes", "2017-09-10")
        self.assertEqual(self.user.shoppinglists["HKUA452SA"].name,
                         "Clothes",
                         "The shopping list name has changed to clothes")
        self.assertEqual(self.user.shoppinglists["HKUA452SA"].notify_date,
                         "2017-09-10", "The notify date must be 2017-09-10")

        # Trying to edit a non-existent shopping list should return False. In
        # this case, We don't have a shopping list with an ID HshfnaA and
        # neither do we have any list called beans.
        self.assertFalse(self.user.edit_shoppinglist(
            "HshfnaA", "Beans", "2018-01-01"))
        self.assertEqual(self.user.shoppinglists["HKUA452SA"].name,
                         "Clothes", "The name never changed from Clothes")

    def test_get_shoppinglist(self):
        self.user.create_shoppinglist(ShoppingList(
            "HDYIAM728", "Clothes", "2018-09-12"))
        self.assertEqual(len(self.user.shoppinglists), 1,
                         "Length of shopping list on user account  is 1")
        self.user.create_shoppinglist(ShoppingList(
            "HS6742SF", "Vegetables", "2018-10-23"))
        self.assertEqual(len(self.user.shoppinglists), 2,
                         "Length of shopping lists on user account is 2")

        shoppinglist = self.user.get_shoppinglist("HS6742SF")
        self.assertEqual(shoppinglist.name, "Vegetables")

        # if user has no shoppinglist with that name
        new_shopping_list = self.user.get_shoppinglist("HSafd42SF")
        self.assertFalse(new_shopping_list)  # new_shopping_list = None


if __name__ == "__main__":
    unittest.main()
