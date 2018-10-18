class BaseItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def update_description(self, new_description):
        raise NotImplementedError()

    def observe(self):
        raise NotImplementedError()

    def touch(self):
        raise NotImplementedError()
