class Game:
    def __init__(self):
        self.pins = 0

    def roll(self, param):
        self.pins += param
        pass

    def score(self):
        return self.pins
