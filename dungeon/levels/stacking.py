_ = None

UH_DESCR = 'You hear funky loops'
DH_DESCR = 'The silky groove makes you want to dance'


class GotTired(Exception):
    ''' Sometimes we overestimate our strength '''


def deep_house(player, description=DH_DESCR):
    _  # even though you are at the bottom
    _  # you can still travel (u)p and d(own) the stack

    player.inventory.append('staircase key')  # ah, here it is!
    return player


def underground_house(player, description=UH_DESCR):
    _
    _  # check (w)here you are now

    _  # unfortunately no key here
    player = deep_house(player)  # must be there.
    return player


def staircase(player, floor=0):
    if floor < -3000:
        # you finally made it!
        player.inventory.append('level key')
        return player  # you dash up the floors like a bullet
    try:
        return staircase(player, floor=floor-1)  # we need to go deeper
    except RecursionError:
        import sys
        print(sys.getrecursionlimit())
        raise GotTired(f'You fell asleep on the {floor}th floor')


def stacking_corridor(player):  # (s)tep in..

    _  # check (w)here you are now

    _ # you find a stairwell door
    if player.inventory.pop() == 'staircase key':
        player = staircase(player)  # unfortunately it's locked

    player = underground_house(player)  # could the key be in(s)ide?

    if player.inventory.pop() == 'staircase key':
        player = staircase(player)

    player.inventory.append('stacking key')
    return player
