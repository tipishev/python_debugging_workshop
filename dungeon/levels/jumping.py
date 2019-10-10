from deaths import SmashedByBoulder, DoomedToDeath

_ = None


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
    raise SmashedByBoulder('This was avoidable...')
    _  # quick! (j)ump here!
    raise SmashedByBoulder('Also avoidable')  # now carefully (n)ext here...
    _  # don't make (n)ext (s)tep! (j)ump here or to the next line
    safe_room(player)  # (s)tep in this room, it's safe as milk.
    _
    a_room_of_certain_doom(player)  # you've been warned
    _  # pst! The key guardian likes bread and beer and hates beards!
    _
    # TODO example of finally and loops where jump doesn't work
    _
    player.inventory.append('b')
    player.inventory[-1] += 'e'
    player.inventory[-1] += 'a'
    player.inventory[-1] += 'r'
    player.inventory[-1] += 'd'
    _
    _
    _
    # TODO work on guardian character
    if player.inventory.pop() in ('bread', 'beer'):
        player.inventory.append('jumping key')
        return player
    else:
        raise DoomedToDeath('go shave!')
