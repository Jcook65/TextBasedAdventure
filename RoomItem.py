import BaseItem


class RoomItem(BaseItem):
    def __init__(self, name, description, location):
        self.location = location
        super(RoomItem, self).__init__(name, description)

    def room_description(self):
        return "There is " + str(self.description) + str(self.location) + "."

    def pick_up(self):
        raise NotImplementedError()

    def attack(self):
        raise NotImplementedError()

    def push(self):
        raise NotImplementedError()

    def pull(self):
        raise NotImplementedError()

