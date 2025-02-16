MAX_PINS = 10


class Frame:
    def __init__(self):
        self.first_roll: int or None = None
        self.__second_roll: int or None = None

    def roll(self, pins_down: int):
        if self.first_roll is None:
            self.first_roll = pins_down
            return

        if self.__second_roll is None:
            self.__second_roll = pins_down

    def is_over(self):
        if self.is_strike():
            return True

        return self.first_roll is not None and self.__second_roll is not None

    def score(self):
        return self.first_roll + self.__second_roll if self.__second_roll is not None else self.first_roll

    def is_spare(self):
        return self.first_roll != MAX_PINS and self.score() == MAX_PINS

    def is_strike(self):
        return self.first_roll == MAX_PINS
