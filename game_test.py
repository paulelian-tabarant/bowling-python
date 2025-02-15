import unittest

from game import Game


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_has_zero_total_score_when_gutter_ball(self):
        for roll in range(20):
            self.game.roll(0)

        self.assertEqual(0, self.game.score())

    def test_adds_pins_from_each_roll_when_3(self):
        for roll in range(20):
            self.game.roll(3)

        self.assertEqual(20 * 3, self.game.score())

    def test_doubles_first_roll_of_next_square_when_a_spare_is_made(self):
        self.game.roll(5)
        self.game.roll(5)

        for i in range(18):
            self.game.roll(3)

        self.assertEqual(5 + 5 + 3 + 18*3, self.game.score())



if __name__ == '__main__':
    unittest.main()
