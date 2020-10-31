class Player:
    def __init__(self, name, selection):
        self.name = name
        self.selection = selection
        self.win_count = 0

    def add_win(self):
        self.win_count +=1