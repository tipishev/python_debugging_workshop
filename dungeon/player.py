class Player:  # TODO inherit from Creature?
    '''
    This class represents your player in the game and you are allowed to
    change only this class.
    '''

    # TODO revisit an `enter` method or a global function
    # TODO move editable parts to a separate file

    def __init__(self, name):
        self.name = name
        self.is_armed = False
        self.hearts = 3
        self.inventory = []

    def __repr__(self):
        return f'this is you, {self.name}'

    def arm(self):
        self.is_armed = True

    def interact(self, other):  # TODO should be a global function
        return (ATTACK, other)

    def pick(self, item):
        # TODO make it adjustable to avoid picking up too much plutonium
        self.inventory.append(item)

        # a splode if carrying too much plutcoin
        plutonium_mass = len([item for item in self.inventory
                              if isinstance(item, PlutCoin)])
        if plutonium_mass >= PLUTONIUM_CRITICAL_MASS:
            raise AtomicallyExploded('you became too enriched')
