MAX_PINS = 10


class Frame:
    def __init__(self):
        self.first_roll: int or None = None
        self.second_roll: int or None = None

    def roll(self, pins_down: int):
        if self.first_roll is None:
            self.first_roll = pins_down
            return

        if self.second_roll is None:
            self.second_roll = pins_down

    def is_over(self):
        return self.first_roll is not None and self.second_roll is not None

    def score(self):
        return self.first_roll + self.second_roll

    def is_spare(self):
        return self.score() == MAX_PINS
