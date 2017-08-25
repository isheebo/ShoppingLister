import string
import random


class App:
    def __init__(self):
        self.registered_users = dict()

    def register(self, user):
        """ register: checks if a User user has been registered by the
        application before.
            :returns True if they are already registered and False otherwise
            :param user: User class
        """
        has_been_registered = False
        if user and user.email not in self.registered_users.keys():
            self.registered_users[user.email] = user
            has_been_registered = True
        return has_been_registered

    def login(self, email, password):
        """ Login tries to login a user with a specified email and password.
        :returns True on success and False otherwise
         """
        if email in self.registered_users:
            user = self.registered_users[email]
            if user.password == password:
                return True
        return False

    def get_user(self, email):
        """
        :param email -- a valid email Address
        get_user: searches the registered_users dictionary for the specified
        email
        :returns a user: User
        """
        if email not in self.registered_users:
            print(
                f"user with email address {email} has not yet been registered")
            return None
        return self.registered_users[email]

    def generate_ID(self):
        return "".join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
