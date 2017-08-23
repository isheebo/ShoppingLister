from datetime import datetime


class User:
    """ A user represents a person using the Application"""

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        # a mapping of ShoppingList IDs to ShoppingList names
        self.shoppinglist_names = dict()
        self.shoppinglists = dict()  # a mapping of shopping list items
