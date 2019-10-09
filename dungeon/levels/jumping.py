# TODO import deaths as avoidable and unavoidable

_ = None


def a_room_of_certain_doom(player):
    _  # Oh.. check (w)here you are
    _  # what has been called cannot be uncalled
    _  # try to go (u)p and (j)ump
    _  #
    _  # didn't help, did it?
    _  # because this is the new bottom frame
    _  # you can still (j)ump within this block [5, 12]
    _  # won't help you though.
    raise Exception('Certain doom as seen on TV')


def jumping_corridor(player):
    # you have to jump a lot here
    _
    _
    raise Exception('smashed by a rock')
    _
    raise Exception('smashed by a rock')
    _
    _
    a_room_of_certain_doom(player)
    _
    player.inventory.append('b')
    player.inventory[-1] += 'e'
    player.inventory[-1] += 'a'
    player.inventory[-1] += 'r'
    player.inventory[-1] += 'd'

    if player.inventory.pop() is 'bread':
        player.inventory.append('jumping key')
        return player
    raise Exception('Failed to collect bread')
