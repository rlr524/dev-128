import random
from dataclasses import dataclass


@dataclass
class Die:
    __value: int

    def get_value(self):
        return self.__value

    def set_value(self, value: int):
        if value < 1 or value > 6:
            raise ValueError("Die value must be from 1 to 6")
        else:
            self.__value = value

    def roll(self):
        self.__value = random.randrange(1, 7)
