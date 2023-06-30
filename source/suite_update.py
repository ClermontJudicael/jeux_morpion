from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont
from music import music_class
from customtkinter import *
import pygame
import random

pygame.mixer.init()
music_obj = music_class()


class audio:
    def __init__(self):

        self.i = random.randint(0, 3)

    def music(self):
        if self.i == 0:
            music_obj.play_music1()
        if self.i == 1:
            music_obj.play_music2()
        if self.i == 2:
            music_obj.play_music3()
        if self.i == 3:
            music_obj.play_music4()


sound = audio()
sound.music()


class Morpion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jeu de Morpion")
        self.window.configure(bg="#3c0384")
        self.current_player = "X"
        self.score_X = 0
        self.score_O = 0

        self.buttons = []
        self.create_gui()

    def create_gui(self):

        # création du frame pour contenir les boutons
        self.frame1 = CTkFrame(
            self.window, fg_color="#4ffaff", width=380, height=380, corner_radius=24)
        self.frame1.grid(row=0, column=1, pady=16, padx=16)
        # Création des boutons

        for i in range(3):
            row = []
            for j in range(3):
                button = CTkButton(self.frame1, text=" ", width=150, height=150,
                                   command=lambda i=i, j=j: self.button_click(i, j), fg_color="#5801c6", corner_radius=24)
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

        # Création du cadre pour les scores et les boutons
        score_frame = CTkFrame(self.window, corner_radius=16, width=450)
        score_frame.configure(fg_color="#2e0266")
        score_frame.grid(row=0, column=4, rowspan=5, padx=20)

        # Créer une police avec la taille du score
        # police_TITRE = tkfont.Font(size=40)
        police_score = tkfont.Font(size=29)
        police_X = tkfont.Font(size=20)
        police_0 = tkfont.Font(size=20)

        # Étiquettes pour afficher les scores
        CTkLabel(score_frame, text="DIF'JAM", font=("Rubik black", 50)).grid(
            row=0, column=0, columnspan=2, pady=30)
        CTkLabel(score_frame, text="Score", font=("Rubik bold", 30)).grid(
            row=2, column=0, columnspan=2)
        CTkLabel(score_frame, text="Joueur X:", font=(
            "Rubik bold", 20)).grid(row=3, column=0, pady=16)
        self.label_score_X = CTkLabel(
            score_frame, text="0", font=("Rubik bold", 20))
        self.label_score_X.grid(row=3, column=1)
        CTkLabel(score_frame, text="Joueur O:", font=(
            "Rubik bold", 20)).grid(row=4, column=0, pady=16)
        self.label_score_O = CTkLabel(
            score_frame, text="0", font=("Rubik bold", 20))
        self.label_score_O.grid(row=4, column=1)

        # Boutons pour nouvelle partie et refaire
        CTkButton(score_frame, text="Nouvelle partie", command=self.new_game, width=250,
                  height=70, font=("Rubik bold", 20), fg_color="#e773ff").grid(row=5+2, column=0, columnspan=2, pady=3)

        CTkButton(score_frame, text="Refaire", command=self.reset_scores, width=250,
                  height=70, font=("Rubik bold", 20), fg_color="#e773ff").grid(row=6+2, column=0, columnspan=2, padx=60, pady=30)

    def button_click(self, i, j):
        global text
        button = self.buttons[i][j]
        text = button.cget("text")
        if text == " ":
            music_obj.play_soundX()
            text = self.current_player
            if self.check_winner():
                music_obj.win()
                messagebox.showinfo(
                    "Fin de partie", f"Le joueur {self.current_player} a gagné !")
                if self.current_player == "X":
                    self.score_X += 1
                    self.label_score_X["text"] = str(self.score_X)
                else:
                    self.score_O += 1
                    self.label_score_O["text"] = str(self.score_O)
                self.new_game()
            elif self.check_draw():
                music_obj.loose()
                messagebox.showinfo("Fin de partie", "Match nul !")
                self.new_game()
            else:
                music_obj.play_soundO()
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        board = [[text for button in row] for row in self.buttons]

        # Vérification des lignes
        for row in board:
            if row[0] == row[1] == row[2] != " ":
                return True

        # Vérification des colonnes
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] != " ":
                return True

        # Vérification des diagonales
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return True
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return True

        return False

    def check_draw(self):
        board = [[text for button in row] for row in self.buttons]
        return all(board[i][j] != " " for i in range(3) for j in range(3))

    def new_game(self):
        music_obj.clic()
        for row in self.buttons:
            for button in row:
                button["text"] = " "
        self.current_player = "X"

    def reset_scores(self):
        music_obj.clic()
        self.score_X = 0
        self.score_O = 0
        self.label_score_X["text"] = "0"
        self.label_score_O["text"] = "0"

    def run(self):
        self.window.mainloop()


morpion_game = Morpion()
morpion_game.run()
