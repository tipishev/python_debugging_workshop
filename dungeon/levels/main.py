from .walking import walking_corridor
from .looking import looking_corridor
from .jumping import jumping_corridor
from .stacking import stacking_corridor


class EatenByRat(Exception):
    ''' a fate no worse than death, just more humiliating '''


def main_corridor(player):

    #  if not player.inventory:
    #      raise EatenByRat('Do not go empty-handed!')

    # TODO 'foo key' -> 'amulet of foo'
    if 'walking key' not in player.inventory:
        breakpoint()
        player = walking_corridor(player)

    #  if 'looking key' not in player.inventory:
    #      player = looking_corridor(player)

    if 'stacking key' not in player.inventory:
        player = stacking_corridor(player)

    #  if 'jumping key' not in player.inventory:
    #      player = jumping_corridor(player)


    # TODO add a proper final challenge as final room requiring all keys
    player.inventory.append('Golden Python')
    return player