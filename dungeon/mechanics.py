def enter(player, location):
    if player.dares(location):
        return location(player)

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
