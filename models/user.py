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

    def create_shoppinglist(self, shop_list):
        """ Adds a ShoppingList to a specified user profile.
        """

        if shop_list.list_id in self.shoppinglists or shop_list.name in self.shoppinglist_names.values():
            return False
        self.shoppinglists[shop_list.list_id] = shop_list
        self.shoppinglist_names[shop_list.list_id] = shop_list.name
        return True
