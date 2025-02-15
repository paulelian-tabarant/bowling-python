class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, param):
        self.rolls.append(param)
        pass

    def score(self):
        score = 0

        for i in range(len(self.rolls)):

            if i < 18 and self.rolls[i] + self.rolls[i+1] == 10:
                score += self.rolls[i+2]

            score += self.rolls[i]

        return score

