#!/usr/bin/env python3

__ = "filler oh-oh-oh filler"
PLUTONIUM_CRITICAL_MASS = 11  # kg


def narrate(phrase):
    print(f'*{phrase}*')


def encounter(*actors):
    for actor in actors:
        pass


# TODO fight as a global function

# Items

class Coin:
    """ a plain silver coin
          __,.,---'''''              '''''---..._
       ,-'             .....:::''::.:            '`-.
      '           ...:::.....       '
                  ''':::'''''       .               ,
      |'-.._           ''''':::..::':          __,,-
       '-.._''`---.....______________.....---''__,,-
            ''`---.....______________.....---''
    """


coin = Coin()


class PlutCoin:
    """ a 1 kg plutonium-239 coin
                      ______________
          __,.,---'''''              '''''---..._
       ,-'             .....:::''::.:            '`-.
      '           ...:::.....       '
                  ''':::'''''       .               ,
      |'-.._           ''''':::..::':          __,,-
       '-.._''`---.....______________.....---''__,,-
            ''`---.....______________.....---''

    """


plutcoin = PlutCoin()


class Player:

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
        narrate(f'{self.name} exercises the 2nd ammendment')
        self.is_armed = True
        narrate(f'{self.name} feels safer')

    def fight(self, other):  # TODO should be a global function
        assert self.is_armed
        del other

    def pick(self, item):
        # TODO make it adjustable to avoid picking up too much plutonium
        self.inventory.append(item)

        # a splode if carrying too much plutcoin
        plutonium_mass = len([item for item in self.inventory
                              if isinstance(item, PlutCoin)])
        if plutonium_mass >= PLUTONIUM_CRITICAL_MASS:
            raise AtomicallyExploded('you became too enriched')


class Rat():  # TODO make a Creature superclass

    def __repr__(self):
        return 'A rat'

    def say(self, phrase):
        print(f'Rat: {phrase}')

    def fight(self, player):
        if not player.is_armed:
            raise EatenByRat('maybe you should get a weapon')
        else:
            self.say('Ayeeee!')
            narrate('the rat perishes')

# Exceptions aka Deaths


class EatenByRat(Exception):
    ''' a fate no worse than death, just more humiliating '''


class AtomicallyExploded(Exception):
    ''' unlike whiskey, too much plutonium is too much '''


def entrance(player):
    ''' an entrance to the Dungeons of Doom '''
    #  rat = Rat()
    #  rat.fight(player)
    import ipdb
    ipdb.set_trace(context=5)  # XXX breakpoint
    boring_corridor(player)
    __
    __
    __
    __
    __
    __
    '''
    show ways to stop
    * set a breakpoint
    * until
    '''
    __
    __
    __
    __  # you know
    __  # it can go for quite a while...
    __  # pst! take a look at lines 79 to 80  # FIXME they change
    __
    __
    __
    __
    __
    __
    narrate('nothing to see for for the next 20 lines')
    '''
    * use l for incremental listing
    * use ll for listing
    * use absolute look with n, n+10
    * use absolute look with n, 10  # same as previous
    '''
    __  # l 71,20
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    lower_floor(player, company=[Rat()] * 3)


def boring_corridor(player):
    ''' This is a rather dull looking corridor with grey dusty walls '''
    __
    __
    __
    __
    __
    __  # there's a writing on a dusty wall
    __  # "this corridor is long,
    __  # I promiss, there is nothing
    __  # to see here, just a 5 coins.
    __  # so, just type "r" or "return" to skip to the end of it.
    __
    __
    __
    __
    __
    __
    __
    player.pick(coin)
    __
    __
    __
    __
    __
    __
    player.pick(coin)
    player.pick(coin)
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    player.pick(coin)
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    return 42  # Thanks for walking with us, buh-bye!


def lower_floor(player, company):
    ''' the room is decorated with glowing rocks '''
    narrate('you hear someone following you down the stairs')
    pass


def main_corridor():
    player = Player(name='Tim')

    # Preparation  TODO a separate method or file?
    player.arm()

    entrance(player)


if __name__ == '__main__':
    main_corridor()
