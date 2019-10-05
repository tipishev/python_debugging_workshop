class Rat():  # TODO make a Creature superclass

    def __repr__(self):
        return 'A rat'

    def say(self, phrase):
        print(f'Rat: {phrase}')

    def fight(self, player):
        if not player.is_armed:
            raise EatenByRat('maybe you should get a weapon')
        else:
            self.say('Ayeeee!')
            narrate('the rat perishes')
