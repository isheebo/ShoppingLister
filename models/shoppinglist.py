from datetime import datetime


class ShoppingList:
    def __init__(self, list_id, name, notify_date):
        self.list_id = list_id
        self.name = name
        # date on which to remind the owner of the shopping list
        self.notify_date = notify_date
        self.items = dict()  # dictionary of Items and their IDs (ID: Item)
        self.item_names = dict()  # mapping item names and their IDs (ID: name)
        self.date_created = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.date_modified = self.date_created

    def add_item(self, item):
        """ add_item adds an item to the shopping list. No duplicates allowed
        :returns True if item has been added, False otherwise
        """
        if item.item_id in self.items.keys() or item.name in self.item_names.values():
            return False

        self.items[item.item_id] = item
        self.item_names[item.item_id] = item.name.title()
        self.date_modified = datetime.now().strftime("%Y-%m-%d %H:%M")
        return True

    def remove_item(self, item_id):
        """ Deletes an item from the ShoppingList:
        :param item_id string
        :returns True if item_id exists and has been removed
        False if item with that id hasn't been found
        """
        removed = False
        if item_id in self.items:
            del self.items[item_id]
            del self.item_names[item_id]
            self.date_modified = datetime.now().strftime("%Y-%m-%d %H:%M")
            removed = True
            self.date_modified = datetime.now().strftime("%Y-%m-%d %H:%M")
        return removed

    def get_item(self, item_id):
        """ Returns an item specified by item_id"""
        if item_id in self.items:
            return self.items[item_id]
        return None
