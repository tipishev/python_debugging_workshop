_ = None

def check_password(player):
    password = player.inventory.pop()
    from hashlib import md5
    password = password.encode('utf-8')
    return md5(password).hexdigest() == '4c4e8ca78ae78388276d094f067a04fb'


def a_room(player):
    _  # awesome! glad that you stepped in
    _  # feel free to (s)tep instead of (n)ext
    _  # for non-function lines the result is the same

    _  # (s)tep
    _  # by (s)tep
    _
    _  # you can skip many lines with `(unt)il <line number>`
    _  # in 30 lines there's the level password
    _  # get there with `unt 50`
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _  # fluggaenkoecchicebolsen
    _  # write it down: `!player.inventory.append('fluggaenkoecchicebolsen')`

    _  # there's nothing more to see in this room
    _
    _  # you can fast-forward to the exit with (r)eturn
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _
    return player  # either (n)ext or (s)tep will take you back


def walking_corridor(player):
    _  # type `next` to advance to the next line
    _  # it can be abbreviated to `n`
    _  # let's go to the (n)ext line 3 more times
    _
    _
    _  # you can also press `Enter`
    _  # this repeats the latest debugger command
    _  # ...which is (n)ext in our case

    _  # if you go to the (n)ext line
    _  # on a line with a function call
    _  # it will execute behind the scenes

    player = a_room(player)  # go to the (n)ext line
    _
    _  # what did this room do to you?
    _  # we'll never know...
    _  # unless we (s)tep into it

    player = a_room(player)  # (s)tep inside


    if check_password(player):  # the moment of truth...

        player.inventory.append('walking key')  # woohoo!
        return player


    raise Exception('You are not leaving!')
