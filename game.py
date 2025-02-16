from frame import Frame


def is_not_extra(frame_index):
    return frame_index < 9


class Game:
    def __init__(self):
        self.frames = [Frame()]

    def roll(self, pins_down):
        if self.last_frame().is_over():
            self.frames.append(Frame())

        self.last_frame().roll(pins_down)

    def score(self):
        result = 0

        for frame_index in range(len(self.frames)):
            frame = self.frames[frame_index]

            if is_not_extra(frame_index) and frame.is_spare():
                result += self.spare_bonus_at(frame_index)

            if is_not_extra(frame_index) and frame.is_strike():
                result += self.strike_bonus_at(frame_index)

            result += self.frames[frame_index].score()

        return result

    def strike_bonus_at(self, index):
        if self.frames[index + 1].is_strike():
            return self.nth_frame(index).score() + self.nth_frame(index + 1).first_roll

        return self.nth_frame(index).score()

    def spare_bonus_at(self, index):
        return self.nth_frame(index).first_roll

    def last_frame(self):
        return self.frames[-1]

    def nth_frame(self, number):
        return self.frames[number - 1]
