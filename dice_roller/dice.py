class Dice:
    def __init__(self):
        self.__list = []

    def get_list(self):
        return tuple(self.__list)

    def add_die(self, die):
        self.__list.append(die)

    def roll_all(self):
        for die in self.__list:
            die.roll()