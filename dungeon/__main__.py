#!/usr/bin/env python3


def entrance(player):
    ''' an entrance to the Dungeons of Doom '''
    boring_corridor(player)
    __
    __
    __
    __
    __
    __
    '''
    show ways to stop
    * set a breakpoint
    * until
    '''
    __
    __
    __
    __  # you know
    __  # it can go for quite a while...
    __  # pst! take a look at lines 79 to 80  # FIXME they change
    __
    __
    __
    __
    __
    __
    narrate('nothing to see for for the next 20 lines')
    '''
    * use l for incremental listing
    * use ll for listing
    * use absolute look with n, n+10
    * use absolute look with n, 10  # same as previous
    '''
    __  # l 71,20
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    lower_floor(player, company=[Rat()] * 3)  # TODO hide env with **lower_floor_kwargs


def boring_corridor(player):
    ''' This is a rather dull looking corridor with grey dusty walls '''
    __
    __
    __
    __
    __
    __  # there's a writing on a dusty wall
    __  # "this corridor is long,
    __  # I promiss, there is nothing
    __  # to see here, just a 5 coins.
    __  # so, just type "r" or "return" to skip to the end of it.
    __
    __
    __
    __
    __
    __
    __
    player.pick(coin)
    __
    __
    __
    __
    __
    __
    player.pick(coin)
    player.pick(coin)
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    player.pick(coin)
    __
    __
    __
    __
    __
    __
    __
    __
    __
    __
    return 42  # Thanks for walking with us, buh-bye!


def lower_floor(player, company):
    ''' the room is decorated with glowing rocks '''
    narrate('you hear someone following you down the stairs')
    pass


def main_corridor():
    player = Player(name='Tim')

    # Preparation  TODO a separate method or file?
    player.arm()

    entrance(player)


if __name__ == '__main__':
    main_corridor()
