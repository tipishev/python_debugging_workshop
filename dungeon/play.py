#!/usr/bin/env python3

from player import Player
from levels import jumping_corridor, walking_corridor

player = Player(name='Tim')

player.inventory.append('jumping key')
player.inventory.append('Golden Python')

if not player.has('walking key'):
    #  import ipdb; ipdb.set_trace(context=7)
    player =  walking_corridor(player)

if not player.has('jumping key'):
    #  import ipdb; ipdb.set_trace(context=7)
    player =  jumping_corridor(player)  # you return as a jumpy person

if player and player.has('Golden Python'):
    print('Congratulations, you got the Golden Python!')
else:
    raise Exception('Like many others, you have failed...')

