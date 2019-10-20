from .walking import walking_corridor
from .looking import looking_corridor
from .jumping import jumping_corridor


class EatenByRat(Exception):
    ''' a fate no worse than death, just more humiliating '''


def main_corridor(player):

    if not player.inventory:
        raise EatenByRat('Do not go empty-handed!')

    if not player.has('walking key'):
        player = walking_corridor(player)

    if not player.has('looking key'):
        player = looking_corridor(player)

    if not player.has('jumping key'):
        player = jumping_corridor(player)

    # TODO add a proper final challenge as final room requiring all keys
    player.inventory.append('Golden Python')
    return player
