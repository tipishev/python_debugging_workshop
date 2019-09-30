#!/usr/bin/env python3



def narrate(phrase):
    print(f'*{phrase}*')


# TODO revisit an `enter` method
class Player():

    def __init__(self):
        self.is_armed = False

    def __repr__(self):
        return 'this is you'

    def arm(self):
        self.is_armed = True
        narrate('you feel safer')

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
    pass


# hm.. passing an arg tuple doesn't support deletion, wrap list?
company = [Rat(), Rat(), Rat()]


def entrance(player):
    ''' an entrance to the Dungeons of Doom '''
    rat = Rat()
    rat.fight(player)
    lower_floor(player, *company)


def lower_floor(player, *company):
    ''' the room is decorated with glowing rocks '''
    narrate('you hear someone following you down the stairs')
    pass


def main():
    player = Player()

    # Preparation
    #  player.arm()

    entrance(player)


if __name__ == '__main__':
    main()
