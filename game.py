MAX_PINS = 10


class Frame:
    def __init__(self):
        self.first_roll = None
        self.second_roll = None

    def roll(self, pins_down):
        if self.first_roll is None:
            self.first_roll = pins_down
            return

        if self.second_roll is None:
            self.second_roll = pins_down

    def is_over(self):
        return self.first_roll is not None and self.second_roll is not None


class Game:
    def __init__(self):
        self.rolls = []
        self.frames = [Frame()]

    def roll(self, param):
        self.rolls.append(param)

        last_frame = self.frames[-1]
        if not last_frame.is_over():
            last_frame.roll(param)
            return

        self.frames.append(Frame())

    def score(self):
        score = 0

        for frame in range(len(self.rolls) // 2):
            first_roll = frame * 2
            second_roll = first_roll + 1

            if self.rolls[first_roll] + self.rolls[second_roll] == MAX_PINS:
                score += self.rolls[second_roll + 1]

            score += self.rolls[first_roll] + self.rolls[second_roll]

        return score
