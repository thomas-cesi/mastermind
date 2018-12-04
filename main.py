from tkinter import *
import mastermindapp as m

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
    app = m.MasterMindApp(app_window)

    # boucle principale :
    app_window.mainloop()

if __name__ == '__main__':
    main()
