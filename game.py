from frame import Frame


def is_not_extra(frame_index):
    return frame_index < 10


class Game:
    def __init__(self):
        self.frames = [Frame()]

    def roll(self, pins_down):
        if self.last_frame().is_over():
            self.frames.append(Frame())

        self.last_frame().roll(pins_down)

    def score(self):
        result = 0

        for frame_number in range(1, len(self.frames) + 1):
            frame = self.nth_frame(frame_number)

            if is_not_extra(frame_number) and frame.is_spare():
                result += self.spare_bonus_at(frame_number)

            if is_not_extra(frame_number) and frame.is_strike():
                result += self.strike_bonus_at(frame_number)

            result += frame.score()

        return result

    def strike_bonus_at(self, index):
        if self.frames[index].is_strike():
            return self.nth_frame(index - 1).score() + self.nth_frame(index).first_roll

        return self.nth_frame(index - 1).score()

    def spare_bonus_at(self, index):
        return self.nth_frame(index - 1).first_roll

    def last_frame(self):
        return self.frames[-1]

    def nth_frame(self, number):
        return self.frames[number - 1]
