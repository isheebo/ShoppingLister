import unittest
from models.user import User
from models.shoppinglist import ShoppingList


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
