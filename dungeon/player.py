class Player:

    def __init__(self, name, inventory=None):
        self.name = name
        self.inventory = inventory or []

    def has(self, item):
        return item in self.inventory
