# the password is 'spyglass', sorry no time for puzzle
# `!player.inventory.append('spyglass')`
# `(c)ontinue` will take you to the breakpoint

from mechanics import check_password


_ = None


def check_looking_password(player):
    return check_password(player, '0a5d79f5655a4ace894b62c28ab11083')


def looking_corridor(player):  # please, (s)tep in!
    _  # there are a few ways to look at the source in iPDB
    _  # type `list`
    _
    _  # by default it shows you 11 lines
    _  # 5 above, current line (--->), and 5 below
    _  # abbreviate the command to `l` to see the next 11 lines
    _
    _
    _
    _
    _
    _  # press `Enter` to see the next 11 lines...
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _  # do you have a déjà-vu?
    _  # press `Enter` again...
    _
    _
    _
    _
    _
    _
    _
    _
    _
    _  # if missed something, go back (or forward) with
    _  # `(l)ist {lineno}`
    _  # for example `l 39`
    _
    _
    _
    _
    _  # ...or press `Enter` to keep listing
    _
    _
    _
    _
    _
    _  # you can also specify the range
    _  # with `(l)ist {start_lineno},{last_lineno}`
    _  # try `l 70,76`
    _
    _
    _
    _
    _
    _
    _  # <--- line 70
    _
    _  # since 70 < 76
    _  # 70,76 was interpreted as range
    _  # now try `l 80,10`
    _
    _  # <--- line 76
    _
    _
    _
    _  # <--- line 80
    _
    _
    _  # since 80 > 10
    _  # 80,10 was interpreted as
    _  # "line 80 and 10 lines following it"
    _
    _  # press `l` or `Enter` to continue
    _
    _
    _  # <--- line 80 + 10
    _
    _
    _
    _
    _  # finally, there is `longlist` command
    _  # abbreviated to `ll`
    _  # it lists the whole function
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
    _  # yep, `longlist` shows you the whole function
    _  # scroll up and confirm that the output starts with 'def'
    _
    _  # to stop yourself in front of the Password Room
    _  # type `break 123` and `ll` again
    _  # then (l)ook at lines 1,2,3! `l 1,3`
    _
    return password_room(player)  # (i)f ready (s)tep in...


def password_room(player):
    if check_looking_password(player):  # press (n)ext

        # Once again, you have succeeded!!!
        player.inventory.append('amulet of looking')
        # you also unlock a cheatcode! `alias la l 1,9999`
        return player  # press q to quit

    raise Exception('Incorrect Looking Password')
