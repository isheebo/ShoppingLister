import unittest
from models.mainapp import App
from models.user import User


class MainAppTest(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_register_users(self):
        self.assertTrue(self.app.register(
            User("Kanyesigye Edgar", "kedgar751@gmail.com", "password")))
        self.assertEqual(len(self.app.registered_users), 1,
                         "Only one user has been added!")

        # on trying to register the same user twice, it should return False
        self.assertFalse(self.app.register(
            User("Kanyesigye Edgar", "kedgar751@gmail.com", "password")))
        self.assertEqual(len(self.app.registered_users), 1,
                         "No duplicates allowed: only one user is registered!")
        self.assertTrue(self.app.register(
            User("Muhwezi Allan", "muhallan@gmail.com", "password")))
        self.assertEqual(len(self.app.registered_users), 2,
                         "2nd user added,hence number of registered users = 2")
