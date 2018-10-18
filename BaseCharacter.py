class BaseCharacter:
    def __init__(self, inventory, name, description, hp):
        self.inventory = inventory
        self.name = name
        self.description = description
        self.hp = hp

    def add_inventory(self, item):
        raise NotImplementedError()

    def remove_inventory(self, item):
        raise NotImplementedError()
