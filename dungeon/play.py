#!/usr/bin/env python3

from player import Player
from levels import (
    jumping_corridor,
    walking_corridor,
    looking_corridor,
)

player = Player(name='Tim')

player.inventory.append('jumping key')
player.inventory.append('walking key')

if not player.has('walking key'):
    player =  walking_corridor(player)

if not player.has('looking key'):
    player =  looking_corridor(player)

if not player.has('jumping key'):
    player =  jumping_corridor(player)  # you return as a jumpy person

# TODO add a proper challenge to get the Golden Python
player.inventory.append('Golden Python')

if player and player.has('Golden Python'):
    print('Congratulations, you got the Golden Python!')
else:
    raise Exception('Like many others, you have failed...')

