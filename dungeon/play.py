#!/usr/bin/env python3

from player import Player
from levels import jumping_corridor

player = Player(name='Tim')

import ipdb; ipdb.set_trace(context=3)
player =  jumping_corridor(player)  # you return as a different person

if player and player.has('Golden Python'):
    print('Congratulations!')
else:
    raise Exception('Like many others, you have failed...')

