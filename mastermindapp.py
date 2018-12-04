from Entities import game as g
from Entities import piece as p
from tkinter import *
from tkinter import messagebox

class MasterMindApp:
    def __init__(self, master):
        Button(master, text="Commencer une nouvelle partie", command=self.start_game).grid(row=0, column=0)
        Button(master, text="test", command=self.test).grid(row=0, column=1)

        # --- Configuration de la partie :
        self.score = StringVar()
        self.playerone = StringVar()
        self.playertwo = StringVar()
        self.level = StringVar()
        self.level.trace("w", self.update_level_observer)
        self.debug_mode = BooleanVar()
        self.debug_mode.trace("w", self.update_mode_observer)
        self.config_frame = LabelFrame(master, text="Configuration", width=500, height=350)
        self.player_one_entry = Entry(self.config_frame, textvariable=self.playerone)
        self.player_two_entry = Entry(self.config_frame, textvariable=self.playertwo)
        Label(self.config_frame, text="Veuillez enregistrer les 2 joueurs :").grid(row=1, column=0)
        self.player_one_entry.grid(row=1, column=1)
        self.player_two_entry.grid(row=1, column=2)
        Label(self.config_frame, text="Choix du niveau de diffuculté :").grid(row=2, column=0)
        Radiobutton(self.config_frame, text="Facile", value="facile", variable=self.level).grid(row=2, column=1)
        Radiobutton(self.config_frame, text="Moyen", value= "moyen", variable=self.level).grid(row=2, column=2)
        Label(self.config_frame, text="Activer/Désactiver le mode debug :").grid(row=3, column=0)
        Checkbutton(self.config_frame, text="Mode debug", variable=self.debug_mode, onvalue=1, offvalue=0).grid(row=3, column=1)
        Button(self.config_frame, text="Enregistrer", command=self.set_players).grid(row=4, column=0)

        self.play_btn = Button(master, text="jouer", command=self.solution_entry)
        self.solution_frame = LabelFrame(master, text="Solution", width=700)
        self.try_frame = LabelFrame(master, text="Tentatives", width=700)
        self.attempts_frame = LabelFrame(master, text="score", width=700)
        self.score_label = Label(self.attempts_frame, textvariable=self.score).grid()

    def start_game(self):
        print("Configuration d'une nouvelle partie")
        self.newGame = g.Game()
        self.config_frame.grid(row=5, column=0, ipadx=50, ipady=15)
        self.play_btn.grid(row=6, column=2)

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

    def solution_entry(self):
        print("La partie commence")
        Label(self.solution_frame, text="Joueur 1, saisissez votre suite :").grid(ipadx=50, ipady=15)
        self.newGame.set_solution_entry(self.solution_frame)
        Button(self.solution_frame, text="Valider", command=self.get_solution).grid(ipadx=50, ipady=15)
        self.solution_frame.grid(row=7, column=0)

    def get_solution(self):
        self.solution = []
        for piece in self.newGame.solution_entry.define_combination():
            self.solution.append(piece.piece_color.get())
        print("Au tour du joueur 2")
        Label(self.try_frame, text="Joueur 2, saisissez une suite :").grid(ipadx=50, ipady=15)
        self.newGame.set_try_entry(self.try_frame)
        Button(self.try_frame, text="Valider", command=self.attempts).grid(ipadx=50, ipady=15)
        if self.newGame.debug_mode:
            self.try_frame.grid(row=8, column=0)
            self.attempts_frame.grid(row=9, column=0)
        else :
            self.try_frame.grid(row=7, column=0)
            self.attempts_frame.grid(row=8, column=0)

    def attempts(self):
        print("Check")
        self.newGame.attempts_counter += 1
        if self.newGame.attempts_counter > self.newGame.level['attempts']:
            self.game_over()
            return
        self.attempts = []
        for piece in self.newGame.try_entry.define_combination():
            self.attempts.append(piece.piece_color.get())
        print(self.solution)
        print(self.attempts)
        if self.solution == self.attempts:
            self.newGame.victory = True
            self.victory()
            return
        self.score = ""
        for i, att in enumerate(self.attempts):
            if att == self.solution[i]:
                self.score += '|| ' + att + ' =||'
            elif att in self.solution:
                self.score += '|| ' + att + ' ~||'
            else:
                self.score += '|| ---- ||'
        print(self.score)
        print("Tentative {}".format(self.newGame.attempts_counter))

    def game_over(self):
        messagebox.showinfo("GAME OVER", "partie terminée")

    def victory(self):
        messagebox.showinfo("VICTOIRE", "partie terminée")
