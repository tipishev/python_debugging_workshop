#!/usr/bin/env python3

from player import Player
from levels import entrance, trappy
from mechanics import enter

player = Player(name='Tim')

import ipdb; ipdb.set_trace(context=10)
#  player = enter(player, entrance)
player = enter(player, entrance)

if player and player.has('Golden Python'):
    print('Congratulations!')
else:
    raise Exception('Like many others, you have failed...')

