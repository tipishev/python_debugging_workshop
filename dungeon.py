#!/usr/bin/env python3

import ipdb


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

    def attack(self, other):
        assert self.is_armed
        del other


class Rat():

    def __repr__(self):
        return 'a hideous rodent'

    def say(self, phrase):
        print(f'Rat: {phrase}')

    def attack(self, player):
        if not player.is_armed:
            raise EatenByRat()
        else:
            self.say('Ayeeee!')
            narrate('the rat perishes')


class EatenByRat(Exception):
    pass


# hm.. passing an arg tuple doesn't support deletion, wrap list?
company = [Rat(), Rat(), Rat()]


def entrance(self):
    ''' an entrance to the Dungeons of Doom '''
    ipdb.set_trace(context=5)
    rat = Rat()
    rat.attack(player)
    lower_floor(self, *company)


def lower_floor(self, *company):
    ''' the room is decorated with glowing rocks '''
    narrate('you hear someone following you down the stairs')
    ipdb.set_trace(context=5)
    pass


if __name__ == '__main__':
    player = Player()

    # Preparation
    player.arm()

    entrance(player)
