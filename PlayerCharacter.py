import BaseCharacter


class PlayerCharacter(BaseCharacter):
    def __init__(self, inventory, name, description, hp, stats):
        self.stats = stats
        super(PlayerCharacter, self).__init__(inventory, name, description, hp)

    def take_damage(self):
        pass

    def heal_damage(self):
        pass

    def attack(self):
        pass

    def move(self, direction):
        pass

    def hide(self):
        pass

    def stop(self):
        pass
