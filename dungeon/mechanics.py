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
    password = password.encode('utf-8')
    return md5(password).hexdigest() == hexdigest


def check_walking_password(player):
    return check_password(player,  '4c4e8ca78ae78388276d094f067a04fb')
