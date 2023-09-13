import tkinter as tk
from tkinter import messagebox
from music import music_class
from customtkinter import *
import pygame

pygame.mixer.init()
music_obj = music_class()

"""We use row[] to store the button, and the we store the variable in buttons[]"""


class Morpion:
    def __init__(self):
        self.window = CTk()
        self.window.title("Morpion game")
        self.window.configure(fg_color="#3c0384")
        self.window.geometry("1320x650")
        self.current_player = "X"
        self.score_X = 0
        self.score_O = 0
        self.switch_var = StringVar(value="on")
        self.buttons = []
        self.create_gui()

    """Here we have the function that destroy the actual 3x3 and create a new 6x6
        First we destroy the button, empty the array that contain the 3x3 and store the new 6x6
        these function are called by the switch"""

    def six_six(self):
        for row in self.buttons:
            for button in row:
                button.destroy()
        self.buttons = []

        for i in range(6):
            row = []
            for j in range(6):
                button = CTkButton(self.frame1, text=" ", width=80, height=80,
                                   command=lambda i=i, j=j: self.button_click(i, j), fg_color="#2e0266", hover_color="#5801c6", corner_radius=16, font=("Rubik bold", 32))
                button.grid(row=i, column=j, padx=6, pady=6)
                row.append(button)
            self.buttons.append(row)

    """The same thing for the 3x3"""

    def three_three(self):
        for row in self.buttons:
            for button in row:
                button.destroy()
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = CTkButton(self.frame1, text=" ", width=100, height=100,
                                   command=lambda i=i, j=j: self.button_click(i, j), fg_color="#2e0266", hover_color="#5801c6", corner_radius=16, font=("Rubik bold", 32))
                button.grid(row=i, column=j, padx=8, pady=8)
                row.append(button)
            self.buttons.append(row)

    """Everything about the GUI"""

    def create_gui(self):
        global switch

        self.frame1 = CTkFrame(
            self.window, fg_color="#4ffaff", width=400, height=380, corner_radius=16)
        self.frame1.grid(row=0, columnspan=2, column=4, pady=64, padx=32)

        for i in range(3):
            row = []  # we store every button in row[]
            for j in range(3):
                button = CTkButton(self.frame1, text=" ", width=100, height=100,
                                   command=lambda i=i, j=j: self.button_click(i, j), fg_color="#2e0266", hover_color="#5801c6", corner_radius=16, font=("Rubik bold", 32))
                button.grid(row=i, column=j, padx=8, pady=8)
                row.append(button)
            self.buttons.append(row)  # and then we store row in buttons[]

        score_frame = CTkFrame(self.window, corner_radius=16, width=450)
        score_frame.configure(fg_color="#2e0266")
        score_frame.grid(row=0, column=8, rowspan=5, padx=20, pady=64)

        frame2 = CTkFrame(
            self.window, fg_color="#2e0266", width=380, height=450, corner_radius=16)
        frame2.grid(row=0, column=0, pady=64, padx=32)

        CTkLabel(score_frame, text="Dashboard", font=("Rubik black", 50)).grid(
            row=0, column=0, columnspan=2, pady=30)

        CTkLabel(score_frame, text="Score", font=("Rubik bold", 30)).grid(
            row=2, column=0, columnspan=2)

        CTkLabel(score_frame, text="Player X:", font=(
            "Rubik bold", 20)).grid(row=3, column=0, pady=16)

        CTkLabel(score_frame, text="Player O:", font=(
            "Rubik bold", 20)).grid(row=4, column=0, pady=16)

        self.label_score_X = CTkLabel(
            score_frame, text="0", font=("Rubik bold", 20))
        self.label_score_X.grid(row=3, column=1)

        self.label_score_O = CTkLabel(
            score_frame, text="0", font=("Rubik bold", 20))
        self.label_score_O.grid(row=4, column=1)

        CTkButton(score_frame, text="Restart", command=self.new_game, width=250, fg_color="#5801c6", hover_color="#3c0384",
                  height=70, font=("Rubik bold", 20), corner_radius=64).grid(row=5+2, column=0, columnspan=2, pady=3)
        CTkButton(score_frame, text="New game", command=self.reset_scores, width=250, fg_color="#5801c6", hover_color="#3c0384",
                  height=70, font=("Rubik bold", 20), corner_radius=64).grid(row=6+2, column=0, columnspan=2, padx=60, pady=30)

        switch = CTkSwitch(frame2, text="3x3", command=self.switch,
                           variable=self.switch_var, onvalue="on", offvalue="off", font=("Rubik bold", 16))
        switch.pack(anchor=CENTER, pady=64, padx=64)

    """the switch to switch between 3x3 or 6x6"""

    def switch(self):
        if self.switch_var.get() == "off":
            self.six_six()
            switch.configure(text="6x6")
            self.frame1.configure(pady=12)
        else:
            self.three_three()
            switch.configure(text="3x3")

    """switch value _off_ is for 6x6 and _on_ for 3x3"""

    def check_lines(self):  # row
        if self.switch_var.get() == "off":
            board = [[button.cget("text") for button in row]
                     for row in self.buttons]

            for row in board:
                for i in range(4):
                    if row[i] == row[i+1] == row[i+2] != " ":
                        return True
            return False

        if self.switch_var.get() == "on":
            board = [[button.cget("text") for button in row]
                     for row in self.buttons]
            for row in board:
                if row[0] == row[1] == row[2] != " ":
                    return True
            return False

    def check_columns(self):  # column

        if self.switch_var.get() == "off":
            board = [[button.cget("text") for button in row]
                     for row in self.buttons]
            for j in range(6):
                for i in range(4):
                    if board[i][j] == board[i+1][j] == board[i+2][j] != " ":
                        return True
            return False

        if self.switch_var.get() == "on":
            board = [[button.cget("text") for button in row]
                     for row in self.buttons]
            for j in range(3):
                if board[0][j] == board[1][j] == board[2][j] != " ":
                    return True
            return False

    def check_diagonals(self):

        if self.switch_var.get() == "off":

            board = [[button.cget("text") for button in row]
                     for row in self.buttons]
            for i in range(4):
                for j in range(4):
                    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] != " ":
                        return True
                    if board[i][j+2] == board[i+1][j+1] == board[i+2][j] != " ":
                        return True
            return False
        if self.switch_var.get() == "on":
            board = [[button.cget("text") for button in row]
                     for row in self.buttons]
            if board[0][0] == board[1][1] == board[2][2] != " ":
                return True
            if board[0][2] == board[1][1] == board[2][0] != " ":
                return True

            return False

    def button_click(self, i, j):

        global text
        button = self.buttons[i][j]
        text = button.cget("text")

        if text == " ":
            if self.current_player == "X":
                music_obj.play_soundX()
            if self.current_player == "O":
                music_obj.play_soundO()
            button.configure(text=self.current_player)

            if self.check_winner():
                music_obj.win()
                messagebox.showinfo(
                    "We have a winner", f"Player {self.current_player} won !")
                if self.current_player == "X":
                    self.score_X += 1
                    self.label_score_X.configure(text=str(self.score_X))

                else:
                    self.score_O += 1
                    self.label_score_O.configure(text=str(self.score_O))

                self.new_game()

            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        return True

    def check_winner(self):
        return self.check_lines() or self.check_columns() or self.check_diagonals()

    def new_game(self):
        music_obj.clic()
        self.current_player = "X"
        for row in self.buttons:
            for button in row:
                button.configure(text=" ")

    def reset_scores(self):
        music_obj.clic()
        self.score_X = 0
        self.score_O = 0
        self.label_score_X.configure(text="0")
        self.label_score_O.configure(text="0")
        self.current_player = "X"
        for row in self.buttons:
            for button in row:
                button.configure(text=" ")

    def run(self):
        self.window.mainloop()
