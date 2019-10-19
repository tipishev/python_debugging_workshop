class Player:

    def __init__(self, name):
        self.name = name

        self.inventory = []

    def has(self, item):
        return item in self.inventory
