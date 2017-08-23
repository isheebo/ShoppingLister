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

    def edit_shoppinglist(self, list_id, new_name, notify_date):
        """ Edits the name and the notify_date of an already existing shopping list
        :returns True if the edit is successful. False otherwise
        """
        if list_id in self.shoppinglists:
            old_list = self.shoppinglists[list_id]
            old_list.name = new_name
            old_list.notify_date = notify_date
            old_list.date_modified = datetime.now().strftime("%Y-%m-%d %H:%M")
            return True
        return False

    def get_shoppinglist(self, list_id):
        """ Searches a specified user profile for the specified ShoppingList ID.
        :returns ShoppingList if list_id exists else None
        """
        if list_id in self.shoppinglists:
            # returns a list of Item objects
            return self.shoppinglists[list_id]
        return None
