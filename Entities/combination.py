from tkinter import *
from Entities import piece as p

class Combination(object):
    """docstring for Combination"""

    def __init__(self, level, size, master):
        self.size = size
        self.pieces = []
        self.solution_entry_frame = LabelFrame(master)
        self.number_piece = 1
        while self.number_piece <= size:
            print("piece numéro {}".format(self.number_piece))
            self.pieces.append(p.Piece(level, self.solution_entry_frame, self.number_piece-1))
            self.number_piece += 1
        self.solution_entry_frame.grid()

    def define_combination(self):
        return self.pieces
