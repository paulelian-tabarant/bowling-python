MAX_PINS = 10


def is_over(roll):
    return roll is not None


class Frame:
    def __init__(self):
        self.first_roll = None
        self.__second_roll = None

    def roll(self, pins_down):
        if not is_over(self.first_roll):
            self.first_roll = pins_down
            return

        if not is_over(self.__second_roll):
            self.__second_roll = pins_down

    def is_over(self):
        if self.is_strike():
            return True

        return is_over(self.first_roll) and is_over(self.__second_roll)

    def score(self):
        return self.first_roll + self.__second_roll if is_over(self.__second_roll) else self.first_roll

    def is_spare(self):
        return self.first_roll != MAX_PINS and self.score() == MAX_PINS

    def is_strike(self):
        return self.first_roll == MAX_PINS
