from frame import Frame


def is_not_extra(frame_number):
    return frame_number < 10


class Game:
    def __init__(self):
        self.frames = [Frame()]

    def roll(self, pins_down):
        if self.__last_frame().is_over():
            self.frames.append(Frame())

        self.__last_frame().roll(pins_down)

    def score(self):
        result = 0

        for frame_number in range(1, len(self.frames) + 1):
            frame = self.__nth_frame(frame_number)

            if is_not_extra(frame_number) and frame.is_spare():
                result += self.__spare_bonus_at(frame_number)

            if is_not_extra(frame_number) and frame.is_strike():
                result += self.__strike_bonus_at(frame_number)

            result += frame.score()

        return result

    def __strike_bonus_at(self, n):
        if self.__nth_frame(n + 1).is_strike():
            return self.__nth_frame(n + 1).score() + self.__nth_frame(n + 2).first_roll

        return self.__nth_frame(n + 1).score()

    def __spare_bonus_at(self, n):
        return self.__nth_frame(n + 1).first_roll

    def __last_frame(self):
        return self.frames[-1]

    def __nth_frame(self, number):
        return self.frames[number - 1]
