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

    def last_frame(self):
        return self.frames[-1]

    def score(self):
        result = 0

        # for frame_index in range(len(self.frames)):
        #     frame = self.frames[frame_index]
        #     print(frame.first_roll, frame.second_roll)

        for frame_index in range(len(self.frames)):
            frame = self.frames[frame_index]

            if frame.is_spare() and is_not_extra(frame_index):
                result += self.frames[frame_index + 1].first_roll

            if frame.is_strike() and is_not_extra(frame_index):
                next_frame = self.frames[frame_index + 1]
                next_next_frame = self.frames[frame_index + 2]

                if next_frame.is_strike():
                    result += next_frame.score() + next_next_frame.first_roll
                else:
                    result += self.frames[frame_index + 1].score()

            result += self.frames[frame_index].score()

        return result
