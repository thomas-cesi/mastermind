from tkinter import *
from Entities import game as g

class MasterMindApp:
    def __init__(self, master):
        # variables :
        self.playerone = StringVar()
        self.playertwo = StringVar()
        self.level = StringVar()
        self.level.trace("w", self.update_level_observer)

        # ----- widgets:
        # --- entries :
        self.player_one_entry = Entry(master, textvariable=self.playerone)
        self.player_two_entry = Entry(master, textvariable=self.playertwo)

        # --- labels :
        self.players_selection = Label(master, text="Veuillez enregistrer les 2 joueurs :")
        self.level_selection = Label(master, text="Choix du niveau de diffuculté :")

        # --- buttons :
        self.new_game_button = Button(master, text="Commencer une nouvelle partie", command=self.start_game)
        self.save_players_btn = Button(master, text="Enregistrer", command=self.set_players)
        self.test_btn = Button(master, text="test", command=self.test)

        # --- radios :
        self.level_one_radio = Radiobutton(master, text="Facile", value="facile", variable=self.level)
        self.level_two_radio = Radiobutton(master, text="Moyen", value= "moyen", variable=self.level)

        self.new_game_button.pack()
        self.test_btn.pack()

    def start_game(self):
        print("Début d'une nouvelle partie")
        self.newGame = g.Game()
        self.players_selection.pack()
        self.player_one_entry.pack()
        self.player_two_entry.pack()
        self.save_players_btn.pack()

    def set_players(self, *args):
        self.newGame.set_players(self.player_one_entry.get(), self.player_two_entry.get())
        self.level_selection.pack()
        self.level_one_radio.pack()
        self.level_two_radio.pack()

    def test(self):
        print(self.newGame.player1.nickname)

    def update_level_observer(self, *args):
        self.newGame.set_level(self.level.get())
        print("Niveau choisi : {}".format(self.newGame.level))


def main():
    # création et paramétrage de la fenêtre de l'application :
    app_window = Tk()
    screen_x = int(app_window.winfo_screenwidth())
    screen_y = int(app_window.winfo_screenheight())
    window_x = 800
    window_y = 600
    pos_x = screen_x // 2 - window_x // 2
    pos_y = screen_y // 2 - window_y // 2
    geo = "{}x{}+{}+{}".format(window_x, window_y, pos_x, pos_y)
    app_window.geometry(geo)
    app_window.title("Projet MasterMind")
    app = MasterMindApp(app_window)

    # boucle principale :
    app_window.mainloop()

if __name__ == '__main__':
    main()
