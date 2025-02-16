import unittest

from game import Game


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_has_zero_total_score_when_gutter_ball(self):
        self.rollTimes(20, 0)

        self.assertEqual(0, self.game.score())

    def test_adds_pins_from_each_roll_when_3(self):
        self.rollTimes(20, 3)

        self.assertEqual(20 * 3, self.game.score())

    def test_doubles_first_roll_of_next_frame_when_a_spare_is_made(self):
        self.game.roll(5)
        self.game.roll(5)

        self.rollTimes(18, 3)

        self.assertEqual(5 + 5 + 3 + 18 * 3, self.game.score())

    def test_does_not_consider_ten_pins_on_two_adjacent_frames_as_a_spare(self):
        self.game.roll(3)
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)

        self.rollTimes(16, 0)

        self.assertEqual(5 + 5 + 3 + 3, self.game.score())

    def test_doubles_the_next_frame_when_a_strike_is_made(self):
        self.game.roll(10)

        self.rollTimes(18, 1)

        self.assertEqual(10 + 1 + 1 + 18 * 1, self.game.score())

    def test_gives_an_extra_roll_on_the_11th_frame_when_a_spare_is_made_on_the_10th_frame(self):
        self.rollTimes(18, 0)
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)

        self.assertEqual(5 + 5 + 3, self.game.score())

    def rollTimes(self, times, pins) -> None:
        for roll in range(times):
            self.game.roll(pins)
