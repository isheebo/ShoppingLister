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

    def test_login(self):
        """A person logs in only and only if they are a registered
        app user. Otherwise they can't be logged in"""

        # Because the email is not registered, the user cannot login
        self.assertFalse(self.app.login("kedgar751@gmail.com", "password"))

        # register the user and confirm that it is True
        self.assertTrue(self.app.register(
            User("isheebo", "kedgar751@gmail.com", "password")))

        # Now retry logging in. It should return True
        self.assertTrue(self.app.login("kedgar751@gmail.com", "password"))

        self.assertEqual(len(self.app.registered_users),
                         1, "One user has been registered")

        # Login cannot happen with a wrong password. the function should return
        # False
        self.assertFalse(self.app.login("kedgar751@gmail.com", "Kanyesigye"))

        # Login cannot happen with an unregistered email.
        self.assertFalse(self.app.login("muhallan@gmail.com", "password"))

    def test_get_user(self):
        self.app.register(
            User("Kanyesigye Edgar", "Kedgar751@gmail.com", "password"))
        self.app.register(
            User("Muhwezi Allan", "muhallan@gmail.com", "muhallan"))

        self.assertEqual(len(self.app.registered_users), 2, "Two users added")

        self.app.register(
            User("Kanyesigye Edgar", "Kedgar751@gmail.com", "password"))

        # It doesn't allow a user to be registered twice
        self.assertEqual(len(self.app.registered_users), 2,
                         "Two users added: no duplicates allowed")

        # getting registered user
        user = self.app.get_user("muhallan@gmail.com")
        self.assertTrue(user)
        self.assertEqual(user.name, "Muhwezi Allan",
                         "user with email muhallan@gmail.com is Muhwezi Allan")
        self.assertEqual(user.password, "muhallan",
                         "Password for muhallan@gmail.com is muhallan")

        # Returns None when we try to get an unregistered user
        first_user = self.app.get_user("kad@gmail.com")
        self.assertFalse(first_user)
