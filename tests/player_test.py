import unittest
from app.models.player import Player
from app.models.selection import Selection

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Bob", Selection.ROCK)
        self.player2 = Player("Barbera", Selection.PAPER)
        self.player3 = Player("Margaret", Selection.SCISSORS)

    def test_has_name(self):
        self.assertEqual("Bob", self.player1.name)

    def test_has_selection(self):
        self.assertEqual(Selection.SCISSORS, self.player3.selection)

    def test_has_win_count(self):
        self.assertEqual(0, self.player3.win_count)