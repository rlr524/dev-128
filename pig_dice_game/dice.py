import random
from dataclasses import dataclass


@dataclass
class Die:
    __value: int = 1

    @property
    def value(self):
        return self.__value

    def roll(self):
        self.__value = random.randrange(1, 7)


class Dice:
    def __init__(self):
        self.__list = []

    @property
    def list(self):
        return tuple(self.__list)

    def add_die(self, die):
        self.__list.append(die)

    def roll_all(self):
        for die in self.__list:
            die.roll()
