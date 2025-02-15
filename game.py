MAX_PINS = 10

class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, param):
        self.rolls.append(param)

    def score(self):
        score = 0

        for roll in range(len(self.rolls)):

            if roll < len(self.rolls) - 2 and self.rolls[roll] + self.rolls[roll + 1] == MAX_PINS:
                score += self.rolls[roll + 2]

            score += self.rolls[roll]

        return score
