from datetime import datetime


class Item:
    """ Item defines the properties of ordinary shopping list items"""


    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.date_added = datetime.now().strftime("%Y-%m-%d %H:%M")
