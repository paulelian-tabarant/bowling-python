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
        for i in range(20):
            self.game.roll(3)

        self.assertEqual(60, self.game.score())



if __name__ == '__main__':
    unittest.main()
