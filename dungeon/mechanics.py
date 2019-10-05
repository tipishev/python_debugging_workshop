def interact(*actors):
    '''
    give every actor a list of other actors and collect actor's action
    '''

    for actor in actors:
        action = actor.act(actors - actor):  # don't pass self?

        # execute action
        '''
        action can be one of
        * (ESCAPE)
        * (ATTACK, target)
        * (ITEM, target)
        '''
