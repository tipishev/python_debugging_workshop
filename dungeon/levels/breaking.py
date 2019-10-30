import random
import codecs

from mechanics import check_password

_ = None


class BrakeException(Exception):
    ''' you slow to a halt '''


class Sage:
    def speak(self):
        return ('Jung qbrf bar qevax jura gnxvat n goernx?'
                ' (!cynlre.vairagbel.nccraq(nafjre))')


class Commoner:
    def speak(self):
        return random.choice((
            'V xabj abguvat, fbeel.',
            'Jung qb lbh jnag?',
            'Ab vqrn.',
            'Tbbq dhrfgvba.'
        ))


crowd = 99*[Commoner()] + [Sage()]  # there's a Sage among Commoners
random.shuffle(crowd)  # but where's he?


def check_breaking_password(player):
    return check_password(player, '7239ea2b5dc943f61f3c0a0276c20974')


def breaking_corridor(player):
    _  # (s)tep in, it's the final level!

    _  # rememeber we learned walking?
    _  # (b)reak + (c)ontinue is the spell of teleportation
    _  # `b 50;;c` will stop you on line 50
    _
    _

    # you learn a new language!  # try it with player.translate('Uhyyb!')
    setattr(player, 'translate', lambda s:  codecs.encode(s, 'rot13'))
    _

    _  # the number on the left shows this breakpoint
    _  # type `b` to see all the breakpoints
    _  # here's another spell `j 42;;c;;b` note the hit number

    _  # let's (cl)ear the first breakpoint with `clear 1`
    _
    _  # try `b 52;;b 53;;b 54;;l`
    _  # to clear them all use `clear`
    _

    _  # create a self-destructing breakpoint with `tbreak 65` and `(c)ontinue`
    _
    _
    _
    _
    _  # persistent breakpoints shine in loops: `b 80`
    _
    _
    _
    for person in crowd:
        _  # `person.speak()` could give a hint
    _
    _
    _
    if check_breaking_password(player):  # you k(n)ow the drill!

        # outstanding!
        player.inventory.append('amulet of breaking')
        return player  # please (c)ontinue

    raise BrakeException('Not so fast!')
