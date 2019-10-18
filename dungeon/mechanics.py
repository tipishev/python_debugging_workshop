def interact(*actors):
    '''
    give every actor a list of other actors and collect actor's action
    '''

    for actor in actors:
        action = actor.act(actors - actor)

        # execute action
        '''
        action can be one of
        * (ESCAPE)
        * (ATTACK, target)
        * (ITEM, target)
        '''


def check_password(player, hexdigest):
    password = player.inventory.pop()
    from hashlib import md5
    password = password.encode('utf8')
    return md5(password).hexdigest() == hexdigest
