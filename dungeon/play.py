#!/usr/bin/env python3

from player import Player
from levels import main_corridor


# give your player a name
player = Player(name='Tim')

# provide with initial inventory
player.inventory.extend([
    'walking key',
    #  'looking key',
    'jumping key',
])

# the journey will change you
breakpoint()
player = main_corridor(player)  # (s)tep in carefully...

# TODO add a proper challenge to get the Golden Python
player.inventory.append('Golden Python')

if player and player.has('Golden Python'):
    print('Congratulations, you got the Golden Python!')
else:
    raise Exception('Like many others, you have failed...')
