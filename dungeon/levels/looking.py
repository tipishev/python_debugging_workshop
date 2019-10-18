_ = None


def looking_corridor(player):  # please, (s)tep in!
    _  # there are a few ways to look at the source in PDB
    _  # type `list`
    _
    _  # by default it shows you 11 lines
    _  # 5 above, current line (---->), and 5 below
    _
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
    _  # you can always go back (or forward) with
    _  # `(l)ist {lineno}`
    _  # for example `l 30`
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
    _  # try `l 60,66`
    _
    _
    _
    _
    _
    _
    _  # <--- line 60
    _
    _  # since 60 < 66
    _  # 60,66 was interpreted as range
    _  # now try `l 70,10`
    _
    _  # <--- line 66
    _
    _
    _
    _  # <--- line 70
    _
    _
    _  # since 70 > 10
    _  # 70,10 was interpreted as
    _  # "line 70 and 10 lines following it"
    _
    _  # press `l` or `Enter` to continue
    _
    _
    _  # <--- line 70 + 10
    _
    _
    _
    _
    _  # finally, there is `longlist` command
    _  # abbreviated to `ll`
    _  # it lists the whole current file
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
    _  # you can scroll up to the beginnging of the file
    _  # by the way, the key is there, on the first line.
    _
    _
    #  if check_password(player):  # the moment of truth...

    #      # Good job! You made it!
    #      player.inventory.append('walking key')
    #      return player  # press c to (c)ontinue

    raise Exception('You are not leaving!')
