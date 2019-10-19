#!/usr/bin/env python3

from player import Player
from levels import main_corridor

''' Welcome to the game "The Quest for Golden Python"!  '''

# What's your character's name?
player = Player(name='Tim')

# What will you take to the dungeon?
player.inventory.extend([
    #  'broomstick',
    #  'shield',
    #  'walking key',
    #  'looking key',
    #  'jumping key',
])

# the game starts here
breakpoint()
player = main_corridor(player)

if player.has('Golden Python'):
    print('Congratulations, you got the Golden Python!')
