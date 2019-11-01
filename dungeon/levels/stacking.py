from mechanics import check_password

_ = None


class LostInLegacyCode(Exception):
    ''' and another one bites the dust of this ancient code '''


MAYBE_HINT_1 = "When lazy and don't know go to Stack O......."
MAYBE_HINT_2 = "Hints' wording is a silly whim, my favourite editor is V.."
MAYBE_HINT_3 = "Could it be a real hint? When debugging don't use p...."


def check_stacking_password(player):
    return check_password(player, '129e8109f319870e328cc7a1d5b5cae3')


def that_one_module(player, hint):  # unwillingly (s)tep in..
    _  # check (w)here you are
    _  # this is the rock bottom
    _  # but you can still go (u)p and (d)own
    _  #
    _  # the real hint is `(u)p 2` levels, just (a)sk `locals()`
    return player  # put the hint in your inventory before goi(n)g up!


def legacy_from_3_years_ago(player, hint):
    # it gets only wor(s)e
    return that_one_module(player, MAYBE_HINT_3)


def your_last_summer_code(player, hint):
    # it doe(s)n't end here!
    return legacy_from_3_years_ago(player, hint=MAYBE_HINT_2)


def stacking_corridor(player):  # you (s)tep in
    # and (s)lip into...
    player = your_last_summer_code(player, hint=MAYBE_HINT_1)

    if check_stacking_password(player):  # what's (n)ext?

        # Excellent!
        player.inventory.append('amulet of stacking')
        return player  # press q to (q)uit

    raise LostInLegacyCode('Your mind overflows')
