_ = None


def lower_level(player):
    pass


def staircase(player, floor):
    if floor < -100:  # TODO change to 1000+
        player.inventory.append('level key')
        return player


def stacking_corridor(player):
    _
    _
    _
    staircase(player)
    player.inventory.appened('stacking key')
