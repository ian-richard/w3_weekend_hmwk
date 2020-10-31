import unittest

from app.models.game import *
from app.models.player import *

from app.models.selection import Selection

class GameTest(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Bob", Selection.ROCK)
        self.player2 = Player("Barbera", Selection.PAPER)
        self.player3 = Player("Margaret", Selection.SCISSORS)

        self.game = Game("Game 1", [self.player1, self.player2])

    def test_game_has_2_players(self):
        self.assertEqual(2, len(self.game.players))