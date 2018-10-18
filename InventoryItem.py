import BaseItem


class InventoryItem(BaseItem):
    def __init__(self, name, description, weight):
        self.weight = weight
        super(InventoryItem, self).__init__(name, description)

    def throw(self):
        pass

    def discard(self):
        pass

    def equip(self):
        pass

    def unequip(self):
        pass
