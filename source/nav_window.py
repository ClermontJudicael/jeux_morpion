import tkinter as tk
import subprocess
import sys
import pygame
from customtkinter import *
from PIL import Image, ImageTk
from music import music_class


pygame.mixer.init()
music_obj = music_class()


def play_music():
    sound_effect = pygame.mixer.Sound(
        "C:\\Users\\users\\Desktop\\tic_tac\\music\\nav_music.wav")
    sound_effect.set_volume(1)
    sound_effect.play(-1)  # -1 plays the music in a loop


def clic():
    sound_effect = pygame.mixer.Sound(
        "button_on_clic.wav")
    sound_effect.set_volume(9)
    sound_effect.play()


def on_button_clickX():
    ouvrir_fenetre_jeu()
    music_obj.clic()


def on_click_help():
    ouivrir_help()
    music_obj.clic()


def ouvrir_fenetre_jeu():

    subprocess.Popen(
        [sys.executable, "main.py"])
    fenetre_accueil.destroy()  # Détruit la fenêtre d'accueil


def ouivrir_help():
    subprocess.Popen(
        [sys.executable, "help.py"])
    fenetre_accueil.destroy()  # Détruit la fenêtre d'accueil


def open_help():
    subprocess.Popen(
        [sys.executable, "help.py"]
    )
    fenetre_accueil.destroy()


def creer_fenetre_accueil():
    global fenetre_accueil
    fenetre_accueil = CTk()
    screen_width = fenetre_accueil.winfo_screenwidth()
    screen_height = fenetre_accueil.winfo_screenheight()

    canvas = tk.Canvas(fenetre_accueil, width=1250, height=600)
    canvas.pack()

    image = Image.open(
        "C:\\Users\\users\\Desktop\\tic_tac\\img\\background_image.png")

    # Redimensionner l'image pour correspondre à la taille de la fenêtre
    largeur = fenetre_accueil.winfo_screenwidth()
    hauteur = fenetre_accueil.winfo_screenheight()
    image = image.resize((largeur, hauteur), Image.ANTIALIAS)

    window_width = 1250
    window_height = 600
    window_x = (screen_width - window_width) // 2
    window_y = (screen_height - window_height) // 2

    fenetre_accueil.geometry(
        f"{window_width}x{window_height}+{window_x}+{window_y}")
    # Créer un objet ImageTk pour l'affichage dans Tkinter
    image_tk = ImageTk.PhotoImage(image)

    # Afficher l'image de fond sur le canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)

    # Créer un Frame pour les boutons
    boutons_frame = tk.Frame(canvas)
    boutons_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    boutons_frame.configure(bg="#5801c6")

    # Bouton "Jouer"
    bouton_jouer = CTkButton(
        boutons_frame,
        text="Jouer",
        command=lambda: fenetre_accueil.after(3000, on_button_clickX),
        width=190,
        height=50,
        corner_radius=64,
        font=("Rubik bold", 20),
        fg_color="#e773ff"
    )
    bouton_jouer.grid(row=0, column=0, padx=10)

    bouton1 = CTkButton(
        boutons_frame,
        text="Aide",
        command=lambda: on_click_help(),
        width=190,
        height=50,
        corner_radius=64,
        font=("Rubik bold", 20),
        fg_color="#e773ff"
    )
    bouton1.grid(row=0, column=1, padx=10)

    bouton2 = CTkButton(
        boutons_frame,
        text="About",
        command=lambda: clic(),
        width=190,
        height=50,
        corner_radius=64,
        font=("Rubik bold", 20),
        fg_color="#e773ff"
    )
    bouton2.grid(row=0, column=2, padx=10)

    fenetre_accueil.mainloop()


fenetre_accueil = None
play_music()

# Appel à la fonction pour créer la fenêtre d'accueil
creer_fenetre_accueil()
