_ = None


class RolledOverByBoulder(Exception):
    ''' <insert flat joke here> '''


class DoomedToDeath(Exception):
    ''' A lovecraftian certain death '''


class KickedByGuard(Exception):
    ''' This guard has heavy boots and short temper '''


def room_of_certain_doom(player):
    _
    _  # check (w)here you are
    _  # go (u)p and try to (j)ump...
    _  #
    _  # doesn't work, does it?
    _  # It's because room_of_certain_doom is the bottom frame now
    _  #
    _  # fell free to quit/continue
    _  # and avoid going here next time
    raise DoomedToDeath('CertainDoom™ as seen on TV')


def jumping_corridor(player):
    _
    raise RolledOverByBoulder('This was avoidable...')
    _  # quick! (j)ump here!
    raise RolledOverByBoulder('Also avoidable')  # now carefully (n)ext here...
    _  # don't make (n)ext (s)tep! (j)ump here or to the next line
    _
    room_of_certain_doom(player)  # you've been warned
    _
    _  # I've heard the guard likes bread and beer
    _  # ...and hates beards!
    player.inventory.append('b')
    player.inventory[-1] += 'e'
    player.inventory[-1] += 'a'
    player.inventory[-1] += 'r'
    player.inventory[-1] += 'd'
    _
    # you nervously give the last item you got to the level guard...
    item = player.inventory.pop()
    if item in ('bread', 'beer'):
        player.inventory.append('amulet of jumping')
        return player  # have a safe trip! You can quit now
    else:
        raise KickedByGuard('Standing all day at the bottom of the file '
                            f'and all I get is a stupid "{item}"!')
