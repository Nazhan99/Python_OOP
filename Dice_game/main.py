import random
class Die:

    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value

die = Die()

print(die.value)

die.roll()
print(die.value)


#player class

class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10  #initially 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -=1

    def roll_die(self):
        self._die.roll()


# Testing the player class
my_die = Die()
my_player = Player(my_die, True)

print(my_player.die)

