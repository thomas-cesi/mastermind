from tkinter import *

class Piece:
    """docstring for Piece"""

    _colors_level_one = [
        "bleu",
        "vert",
        "jaune",
        "orange",
        "blanc",
        "noir",
        "rouge",
        "marron"
    ]

    def __init__(self, level, master, column):
        self.piece_color = StringVar()
        self.listbox = Listbox(master, selectmode=SINGLE)
        self.listbox.bind('<<ListboxSelect>>', self.update_color_piece)
        if level == "facile":
            self.colors_list = self._colors_level_one
        for color in self.colors_list:
            self.listbox.insert(END, color)
        self.listbox.grid(row=1, column=column)
        Label(master, text="color", textvariable=self.piece_color).grid(row=0, column=column)

    def update_color_piece(self, e):
        w = e.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.piece_color.set(value)
        print("color: {}".format(value))
