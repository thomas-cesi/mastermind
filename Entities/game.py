from Entities import player as p
from Entities import combination as c

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
        self.victory = False

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

    def set_solution_entry(self, master):
        self.solution_entry = c.Combination(self.level['name'], self.level["combinationLength"], master)

    def set_try_entry(self, master):
        self.try_entry = c.Combination(self.level['name'], self.level["combinationLength"], master)
