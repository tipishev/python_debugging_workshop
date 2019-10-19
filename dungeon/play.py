#!/usr/bin/env python3

from player import Player
from levels import main_corridor

''' Welcome to the game "The Quest for Golden Python"!  '''

# What's your character's name?
player = Player(name='Tim')

# What would you like to start with?
player.inventory.extend([
    'sword',
    'shield',
    #  'walking key',
    #  'looking key',
    #  'jumping key',
])

# the game starts here
player = main_corridor(player)

if player.has('Golden Python'):
    print('Congratulations, you got the Golden Python!')
