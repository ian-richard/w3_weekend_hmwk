import unittest
from app.models.selection import Selection

class SelectionTest(unittest.TestCase):

    def test_rock(self):
        self.assertIsNotNone(Selection.ROCK, "Rock is not defined")
    
    def test_paper(self):
        self.assertIsNotNone(Selection.PAPER, "Paper is not defined")
    
    def test_scissors(self):
        self.assertIsNotNone(Selection.SCISSORS, "Scissors is not defined")