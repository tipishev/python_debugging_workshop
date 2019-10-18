#!/usr/bin/env python3

from player import Player
from levels import (
    jumping_corridor,
    walking_corridor,
    looking_corridor,
)

# give your player a name
player = Player(name='Tim')

# provide with initial inventory
#  player.inventory.append('walking key')
player.inventory.append('looking key')
player.inventory.append('jumping key')

breakpoint()
# TODO move to main_corridor
if not player.has('walking key'):
    player = walking_corridor(player)

if not player.has('looking key'):
    player = looking_corridor(player)

if not player.has('jumping key'):
    player = jumping_corridor(player)  # you return as a jumpy person

# TODO add a proper challenge to get the Golden Python
player.inventory.append('Golden Python')

if player and player.has('Golden Python'):
    print('Congratulations, you got the Golden Python!')
else:
    raise Exception('Like many others, you have failed...')
