from app.models.selection import Selection

class Game:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.game_count = 0

                                ##### Check first players selection and compare it to second players selection if they are not equal #####
    def get_winner(self):
        if self.players[0].selection == self.players[1].selection:
            return None

        if self.players[0].selection == Selection.ROCK:
            if self.players[1].selection == Selection.SCISSORS:
                return self.players[0]
            if self.players[1].selection == Selection.PAPER:
                return self.players[1]

        if self.players[0].selection == Selection.PAPER:
            if self.players[1].selection == Selection.SCISSORS:
                return self.players[1]
            if self.players[1].selection == Selection.ROCK:
                return self.players[0]

        if self.players[0].selection == Selection.SCISSORS:
            if self.players[1].selection == Selection.ROCK:
                return self.players[1]
            if self.players[1].selection == Selection.PAPER:
                return self.players[0]