import BaseRoom


class TestRoom(BaseRoom):
    def init(self, x, y, actionable_items):
        super(TestRoom, self).__init__(x, y, actionable_items)
