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
