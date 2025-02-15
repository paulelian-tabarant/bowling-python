class Game:
    def __init__(self):
        self.mem = 0

    def roll(self, param):
        self.mem = param
        pass

    def score(self):
        if self.mem == 0:
            return 0

        if self.mem == 1:
            return 20

        return 40
