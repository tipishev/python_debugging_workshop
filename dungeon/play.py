#!/usr/bin/env python3

from player import Player
from levels.main import main_corridor

''' Welcome to The Quest for Golden Python! '''

# What's your character's name and starting items?
player = Player(
    name='Tim',
    inventory=[''],
)

# the game starts here
player = main_corridor(player)

if player.has('Golden Python'):
    print('Congratulations, you got the Golden Python!')
