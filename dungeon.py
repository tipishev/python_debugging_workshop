#!/usr/bin/env python3

__ = "filler oh-oh-oh filler"

def narrate(phrase):
    print(f'*{phrase}*')

# TODO fight as a global function


class Player:

    # TODO revisit an `enter` method or a global function

    def __init__(self, name):
        self.name = name
        self.is_armed = False
        self.hearts = 3

    def __repr__(self):
        return f'this is you, {self.name}'

    def arm(self):
        narrate(f'{self.name} exercises the 2nd ammendment')
        self.is_armed = True
        narrate(f'{self.name} feels safer')

    def fight(self, other):
        assert self.is_armed
        del other


class Rat():

    def __repr__(self):
        return 'a hideous rodent'

    def say(self, phrase):
        print(f'Rat: {phrase}')

    def fight(self, player):
        if not player.is_armed:
            raise EatenByRat('maybe you should get a weapon')
        else:
            self.say('Ayeeee!')
            narrate('the rat perishes')


class EatenByRat(Exception):
    ''' a fate no worse than death, but much more humiliating '''


def entrance(player):
    ''' an entrance to the Dungeons of Doom '''
    rat = Rat()
    rat.fight(player)
    import ipdb; ipdb.set_trace(context=5); pass  # XXX breakpoint
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


def lower_floor(player, company):
    ''' the room is decorated with glowing rocks '''
    narrate('you hear someone following you down the stairs')
    pass


def main():
    player = Player(name='Tim')

    # Preparation  TODO a separate method?
    player.arm()

    entrance(player)


if __name__ == '__main__':
    main()
