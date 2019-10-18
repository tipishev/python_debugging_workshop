from .walking import walking_corridor
from .looking import looking_corridor
from .jumping import jumping_corridor

__all__ = ['main_corridor']


def main_corridor(player):
    if not player.has('walking key'):
        player = walking_corridor(player)

    if not player.has('looking key'):
        player = looking_corridor(player)

    if not player.has('jumping key'):
        player = jumping_corridor(player)

    return player
