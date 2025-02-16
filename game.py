from frame import Frame

MAX_PINS = 10


class Game:
    def __init__(self):
        self.rolls = []
        self.frames = [Frame()]

    def roll(self, pins_down):
        self.rolls.append(pins_down)

        if self.frames[-1].is_over():
            self.frames.append(Frame())

        self.frames[-1].roll(pins_down)

    def score(self):
        score = 0

        # for frameIndex in range(len(self.rolls) // 2):
        #     first_roll = frameIndex * 2
        #     second_roll = first_roll + 1
        #
        #     if self.rolls[first_roll] + self.rolls[second_roll] == MAX_PINS:
        #         score += self.rolls[second_roll + 1]

        for frameIndex in range(len(self.frames)):
            frame = self.frames[frameIndex]
            if frame.is_spare():
                next_frame = self.frames[frameIndex + 1]
                score += next_frame.first_roll

            score += self.frames[frameIndex].score()

        return score
