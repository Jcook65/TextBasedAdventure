class BaseRoom:
    def __init__(self, x, y, actionable_items):
        self.x = x
        self.y = y
        self.actionable_items = actionable_items

    def description(self, items):
        raise NotImplementedError()

    def add_item(self, item):
        raise NotImplementedError()

    def remove_item(self, item):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()
