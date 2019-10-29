from mechanics import check_password

_ = None


class FailedExamination(Exception):
    ''' you studied all previous night, but it was not enough '''


def check_examination_password(player):
    return check_password(player, '69c459dd76c6198f72f0c20ddd3c9447')


class Fish:
    ''' it can swim and moralize '''

    def bad_pun(self):
        print('Did you know that I am {self} Fish?')


class Thing:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Thing {self.name}'

    def shake(self, hands):
        print(f'How do you do? Would you like to shake hands with {self}')


bag_of_dicts = [
    {
        'this': 'bag',
        'hint': 'finds',
        'a': ('pa'
              'ss'
              'word'),
        'one': 'in',
    },
    {
        'desires': {
            're'
            'ward': 'shall',
            'having': 'the',
        },
        '"': {
            's'
            'omeon'
            'e': 'who',
        },
    },
    {
        'stripes': '"',
        'type': '!player.inventory.append(answer)',
        'have': 'a', 'h' 'or'
        'se': 'with',
    },
]


def meeting_room(player, fish, thing1, thing2):  # (s)tep in, everyone!
    _  # check who is in with `(a)rgs`
    _  # now check `whatis fish`
    _  # more info with `pinfo fish`
    _  # eye-candy version `pinfo2 fish`
    _  # you can also get the source code for some objects: `source Thing`

    return player  # it's crowded here, let's return


fish = Fish()
thing1 = Thing(1)
thing2 = Thing(2)


def examination_corridor(player):
    breakpoint(context=5)

    # let's (s)tep in and look at the guests
    meeting_room(player, fish, thing1, thing2)

    bag_of_dicts  # you find a peculiar container...
    # examine it with `p` if you miss `print`, and go (n)ext

    _  # or make it pretty with `pp`

    if check_examination_password(player):  # (n)ow you should have a password

        # get outta here, you glorious chap!
        player.inventory.append('amulet of examination')
        return player  # press q

    raise FailedExamination('Please, come again next week')
