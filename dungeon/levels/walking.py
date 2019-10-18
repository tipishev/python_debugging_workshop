from mechanics import check_walking_password
_ = None


def a_room(player):  # sweet! So glad that you stepped in
    _  # feel free to (s)tep instead of (n)ext
    _  # on non-calling lines the result is the same

    _  # (s)tep..
    _  # by (s)tep..
    _
    _  # keep going with `Enter`
    _  # remember, it just repeats the last command.
    _
    _  # you can skip many lines with `(unt)il {line_number}`
    _  # the ⅓ of level password is on line 50
    _  # get there with `until 50`
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
    _
    _
    _
    _  # fluggaen
    _  # pick it up: `!player.inventory.append('fluggaen')`
    _  # the second part is on line 65, try the shorter `unt 65`
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
    _  # koecchi
    _  # `!player.inventory[-1] += 'koecchi'
    _  # the last part is on line 75  `(unt)il 75`
    _
    _
    _
    _
    _
    _
    _
    _  # cebolsen
    _  # `!player.inventory[-1] += 'cebolsen'
    _  # pst! you can use up-arrow to reuse a typed command

    _  # there is nothing else to see in this room
    _  # you can fast-forward to the exit with (r)eturn
    _
    _
    _
    _  # seriously, nothing to see...
    _  # go to (r)eturn
    _
    _
    _  # ok. Here's a joke.
    _  # "Once a a programmer was told: 'while outside, buy milk'...
    _  # ...he never returned."
    _  #
    _  # but you should. Please press `r` now.
    _
    _
    _
    _
    _
    _
    _  # Thank you for walking with us, buh-bye!
    return player  # either (n)ext or (s)tep will take you back


def walking_corridor(player):
    _  # type `next` to advance to the next line
    _  # it can be abbreviated to `n`
    _  # let's go to the (n)ext line 3 more times
    _

    _  # you can also press `Enter`
    _  # this repeats the latest debugger command
    _  # ...which is (n)ext in our case

    _  # if you go to the (n)ext line
    _  # on a line with a function call..
    _  # ..it will execute behind the scenes

    player = a_room(player)  # go to the (n)ext line
    _
    _  # what did this room do to you?
    _  # we'll never know...
    _  # unless we (s)tep into it

    player = a_room(player)  # (s)tep inside

    if check_walking_password(player):  # the mome(n)t of truth...

        # Good job! You made it!
        player.inventory.append('walking key')
        return player  # press c to (c)ontinue

    raise Exception('You are not leaving!')
