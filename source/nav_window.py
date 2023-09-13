import tkinter as tk
import subprocess
import sys
import pygame
from customtkinter import *
from PIL import Image, ImageTk
from music import music_class
import os


pygame.mixer.init()
music_obj = music_class()


def play_music():
    sound_effect = pygame.mixer.Sound(
        "./music/nav_music.wav")
    sound_effect.set_volume(1)
    sound_effect.play(-1)  # -1 plays the music in a loop


def clic():
    sound_effect = pygame.mixer.Sound(
        "button_on_clic.wav")
    sound_effect.set_volume(9)
    sound_effect.play()


"""here we open the main window by calling main.py"""


def open_window():
    subprocess.Popen(
        [sys.executable, "./source/main.py"])
    nav_bar.destroy()


def create_nav_bar():
    global nav_bar
    nav_bar = CTk()
    screen_width = nav_bar.winfo_screenwidth()
    screen_height = nav_bar.winfo_screenheight()

    canvas = tk.Canvas(nav_bar, width=1250, height=600)
    canvas.pack()

    image = Image.open(
        "./img/background_image.png")

    """we have to get the size of the window to resize the image"""
    width = nav_bar.winfo_screenwidth()
    heigth = nav_bar.winfo_screenheight()
    image = image.resize((width, heigth), Image.ANTIALIAS)

    window_width = 1250
    window_height = 600
    window_x = (screen_width - window_width) // 2
    window_y = (screen_height - window_height) // 2

    nav_bar.geometry(
        f"{window_width}x{window_height}+{window_x}+{window_y}")
    image_tk = ImageTk.PhotoImage(image)

    canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)

    frame_for_button = tk.Frame(canvas)
    frame_for_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    frame_for_button.configure(bg="#5801c6")

    play_button = CTkButton(
        frame_for_button,
        text="Play",
        command=lambda: open_window(),
        width=190,
        height=50,
        corner_radius=64,
        font=("Rubik bold", 20),
        fg_color="#e773ff"
    )
    play_button.grid(row=0, column=0, padx=10)
    nav_bar.mainloop()


nav_bar = None
play_music()
create_nav_bar()
