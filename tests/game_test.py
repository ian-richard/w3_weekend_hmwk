import unittest

from app.models.game import *
from app.models.player import *

from app.models.selection import Selection

class GameTest(unittest.TestCase):
    def setUp(self):
        self.rock = Player("Bob", Selection.ROCK)
        self.paper = Player("Barbera", Selection.PAPER)
        self.scissors = Player("Margaret", Selection.SCISSORS)

        self.game = Game("Game 1", [self.rock, self.paper])

    def test_game_has_2_players(self):
        self.assertEqual(2, len(self.game.players))


                    ##### ROCK TESTS #####
    def test_game_has_winner_for_rock(self):
        self.assertEqual(self.paper, self.game.get_winner())

    def test_game_has_winner_for__rock(self):
        self.game.players[1] = self.scissors
        self.assertEqual(self.rock, self.game.get_winner())

    def test_game_has_winner_for_draw(self):
        self.game.players[1] = self.rock
        self.assertEqual(None, self.game.get_winner())

    
                    ##### SCISSORS TESTS #####
    def test_game_has_winner_for_scissors(self):
        self.game.players[0] = self.scissors
        self.game.players[1] = self.paper
        self.assertEqual(self.scissors, self.game.get_winner())

    def test_game_has_winner_for__scissors(self):
        self.game.players[0] = self.scissors
        self.game.players[1] = self.paper
        self.assertEqual(self.scissors, self.game.get_winner())

    def test_game_returns_none_for__draw(self):
        self.game.players[0] = self.scissors
        self.game.players[1] = self.scissors
        self.assertEqual(None, self.game.get_winner())
    

                    ##### PAPER TESTS #####
    def test_game_has_winner_for_paper(self):
        self.game.players[0] = self.paper
        self.game.players[1] = self.rock
        self.assertEqual(self.paper, self.game.get_winner())

    def test_game_has_winner_for__paper(self):
        self.game.players[0] = self.paper
        self.game.players[1] = self.scissors
        self.assertEqual(self.scissors, self.game.get_winner())

    def test_game_returns_none_for___draw(self):
        self.game.players[0] = self.paper
        self.game.players[1] = self.paper
        self.assertEqual(None, self.game.get_winner())