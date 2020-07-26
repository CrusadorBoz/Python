import unittest
import bowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = bowlingGame.BowlingGame()

    # def test_GutterGame(self):
    #     self.rollMany(0,20)
    #     assert self.game.score() == 0
    #
    # def test_AllOnes(self):
    #     self.rollMany(1,20)
    #     assert self.game.score() == 20
    #
    def test_OneSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.game.rollMany(0,17)
        assert self.game.score() == 16
    #
    # def test_OneStrike(self):
    #     self.rollMany(0,19)
    #     self.game.roll(10)
    #     self.game.roll(10)
    #     assert self.game.score() == 20
    #
    # def test_PerfectGame(self):
    #     self.rollMany(10,12)
    #     assert self.game.score() == 300
    #
    # def test_AllSpare(self):
    #     self.rollMany(5,21)
    #     assert self.game.score() == 150

    # def rollMany(self, pins, rolls):
    #     for i in range(rolls):
    #         self.game.roll(pins)
