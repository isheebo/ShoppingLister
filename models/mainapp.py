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
