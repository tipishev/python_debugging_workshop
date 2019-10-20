_ = None


class RolledOverByBoulder(Exception):
    ''' <insert flat joke here> '''


class DoomedToDeath(Exception):
    ''' A lovecraftian certain death '''


class KickedByGuard(Exception):
    ''' This guard has heavy boots and short temper '''


def a_room_of_certain_doom(player):
    _  # Oh-oh...
    _  # this room does NOT return you safely.
    _  #
    _  # fell free to c(ont(inue)), die,
    _  # and avoid going here next time
    raise DoomedToDeath('CertainDoom™ as seen on TV')


def safe_room(player):
    _  # check (w)here you are
    _  # go (u)p and try to (j)ump...
    _
    _  # doesn't work, does it?
    _  # It's because safe_room is the bottom frame now
    _  # you can still (j)ump within this function
    _  # as soon as you (r)eturn to the frame above
    _  # try to (j)ump again
    _
    return player


def jumping_corridor(player):
    ''' here you should j(ump) a lot '''
    _
    _
    raise RolledOverByBoulder('This was avoidable...')
    _  # quick! (j)ump here!
    raise RolledOverByBoulder('Also avoidable')  # now carefully (n)ext here...
    _  # don't make (n)ext (s)tep! (j)ump here or to the next line
    safe_room(player)  # (s)tep in this room, it's safe as milk.
    _
    a_room_of_certain_doom(player)  # you've been warned
    _
    _
    try:  # step in, it's pretty safe
        raise RolledOverByBoulder('except... will save you')
    except RolledOverByBoulder:
        _  # told you.
        _  # Jump to `finally` from here to get a segfault
    finally:
        _  # try to jump out of here
        _  # docs say it's impossible
        _  # they are lying tho
    _
    _  # I've heard the guard likes bread and beer
    _  # ...and hates them beards!
    player.inventory.append('b')
    player.inventory[-1] += 'e'
    player.inventory[-1] += 'a'
    player.inventory[-1] += 'r'
    player.inventory[-1] += 'd'
    _
    _
    _
    # you nervously give the last item you got to the level guard...
    item = player.inventory.pop()
    if item in ('bread', 'beer'):
        player.inventory.append('jumping key')
        return player
    else:
        raise KickedByGuard('Standing all day at the bottom of the file '
                            f'and all I get is a stupid "{item}"!')
