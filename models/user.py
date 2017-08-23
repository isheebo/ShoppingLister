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

    def delete_shoppinglist(self, list_id):
        """ Deletes a shopping list from a specified user profile.
        :param list_id is the id of the ShoppingList to be deleted """

        is_deleted = False
        if list_id in self.shoppinglists:
            del self.shoppinglists[list_id]
            del self.shoppinglist_names[list_id]
            is_deleted = True
        return is_deleted
