import unittest
import bowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = bowlingGame.BowlingGame()

    def test_GutterGame(self):
        self.game.rollMany(0,20)
        assert self.game.score() == 0
        print(self.game.score())

    def test_AllOnes(self):
        self.game.rollMany(1,20)
        assert self.game.score() == 20
        print(self.game.score())

    def test_OneSpare(self):
        self.game.roll(3)
        self.game.roll(7)
        self.game.roll(3)
        self.game.rollMany(0,17)
        assert self.game.score() == 16

    def test_OneStrike(self):
        self.game.rollMany(0,18)
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(3)
        assert self.game.score() == 16

    def test_PerfectGame(self):
        self.game.rollMany(10,12)
        assert self.game.score() == 300

    def test_AllSpare(self):
        self.game.rollMany(5,21)
        assert self.game.score() == 150
