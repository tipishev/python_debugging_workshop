class Player:  # TODO inherit from Creature?
    '''
    This class represents your player in the game and you are allowed to
    change only this class.
    '''

    def __init__(self, name):
        self.name = name
        self.inventory = ['sword', 'shield']

    def has(self, item):
        return item in self.inventory

    def interact(self, *others):
        ''' return a single action '''
        return (ATTACK, other)

    def dares(self, location):
        return False  # let's play it safe for now

    def rename(self):
        self.name = 'Foomba'
        return 'Foomba'
