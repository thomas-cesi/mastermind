from Entities import game as g
from tkinter import *

class MasterMindApp:
    def __init__(self, master):
        # variables :
        self.playerone = StringVar()
        self.playertwo = StringVar()
        self.level = StringVar()
        self.level.trace("w", self.update_level_observer)
        self.debug_mode = BooleanVar()
        self.debug_mode.trace("w", self.update_mode_observer)


        # --- Configuration de la partie :
        self.config_frame = LabelFrame(master, text="Configuration", width=500, height=350)
        self.player_one_entry = Entry(self.config_frame, textvariable=self.playerone)
        self.player_two_entry = Entry(self.config_frame, textvariable=self.playertwo)
        Label(self.config_frame, text="Veuillez enregistrer les 2 joueurs :").pack()
        self.player_one_entry.pack()
        self.player_two_entry.pack()
        Label(self.config_frame, text="Choix du niveau de diffuculté :").pack()
        Radiobutton(self.config_frame, text="Facile", value="facile", variable=self.level).pack()
        Radiobutton(self.config_frame, text="Moyen", value= "moyen", variable=self.level).pack()
        Label(self.config_frame, text="Activer/Désactiver le mode debug :").pack()
        Checkbutton(self.config_frame, text="Mode debug", variable=self.debug_mode, onvalue=1, offvalue=0).pack()
        Button(self.config_frame, text="Enregistrer", command=self.set_players).pack()

        # --- buttons :
        self.new_game_button = Button(master, text="Commencer une nouvelle partie", command=self.start_game)
        self.test_btn = Button(master, text="test", command=self.test)
        self.play_btn = Button(master, text="jouer", command=self.play)

        self.new_game_button.pack()
        self.test_btn.pack()

    def start_game(self):
        print("Configuration d'une nouvelle partie")
        self.newGame = g.Game()
        self.config_frame.pack()
        self.play_btn.pack()

    def set_players(self, *args):
        self.newGame.set_players(self.player_one_entry.get(), self.player_two_entry.get())

    def test(self):
        print(self.newGame.player1.nickname)

    def update_level_observer(self, *args):
        self.newGame.set_level(self.level.get())
        print("Niveau choisi : {}".format(self.newGame.level))

    def update_mode_observer(self, *args):
        self.newGame.set_mode(self.debug_mode.get())
        print("Mode debug : {}".format(self.newGame.debug_mode))

    def play(self):
        print("La partie commence")
