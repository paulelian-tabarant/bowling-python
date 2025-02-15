import unittest

from game import Game


class MyTestCase(unittest.TestCase):
    def test_has_zero_total_score_when_gutter_ball(self):
        game = Game()
        for i in range(20):
            game.roll(0)

        self.assertEqual(0, game.score())

    def test_adds_pins_from_each_roll_when_3(self):
        game = Game()
        for i in range(20):
            game.roll(3)

        self.assertEqual(60, game.score())


if __name__ == '__main__':
    unittest.main()
