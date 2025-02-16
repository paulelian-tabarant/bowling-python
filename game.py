MAX_PINS = 10


class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, param):
        self.rolls.append(param)

    def score(self):
        score = 0

        for frame in range(len(self.rolls) // 2):
            first_roll = frame * 2
            second_roll = first_roll + 1

            if self.rolls[first_roll] + self.rolls[second_roll] == MAX_PINS:
                score += self.rolls[second_roll + 1]

            score += self.rolls[first_roll] + self.rolls[second_roll]

        return score
