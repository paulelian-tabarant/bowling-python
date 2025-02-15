class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, param):
        self.rolls.append(param)
        pass

    def score(self):
        return sum(self.rolls)
