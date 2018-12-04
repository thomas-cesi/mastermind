from Entities import player as p

class Game:
    """docstring for Game"""

    _level_one = {
        "name": "facile",
        "combinationLength": 4,
        "colors": 8,
        "attempts": 10
    }

    _level_two = {
        "name": "moyen",
        "combinationLength": 6,
        "colors": 10,
        "attempts": 10
    }

    def __init__(self):
        self.attempts_counter = 0
        self.attempts_array = []

    def set_players(self, player1, player2):
        self.player1 = p.Player(player1)
        self.player2 = p.Player(player2)

    def set_level(self, level):
        if(level == self._level_one['name']):
            self.level = self._level_one
        else :
            self.level = self._level_two

    def set_mode(self, mode):
        self.debug_mode = mode


    def set_Solution(self, solution):
        self.solution = solution
