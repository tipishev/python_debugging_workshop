#!/usr/bin/env python3

from levels.main import main_corridor


class Player:

    def __init__(self, name, inventory=None):
        self.name = name
        self.inventory = inventory or []


''' Welcome to The Quest for Golden Python! '''

# What's your character's name and starting items?
player = Player(
    name='',
    inventory=[''],
)

# the game starts here
player = main_corridor(player)

if 'Golden Python' in player.inventory:
    print('Congratulations, you got the Golden Python!')
