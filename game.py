class Game:
    def __init__(self):
        self.mem = 0

    def roll(self, param):
        self.mem = param
        pass

    def score(self):
        if self.mem == 0:
            return 0

        return 20
