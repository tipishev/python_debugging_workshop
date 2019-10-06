#!/usr/bin/env python3

from player import Player
from levels import entrance
from mechanics import enter

player = Player(name='Tim')

player = enter(player, entrance)

if player and player.has('Golden Python'):
    print('Congratulations!')
else:
    raise Exception('Like many others, you have failed...')

