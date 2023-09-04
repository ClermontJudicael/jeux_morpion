from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont
from music import music_class
from customtkinter import *
import pygame
import random
from function import Morpion

# the actual game doesn't support player vs computer
# maybe in the future i will add it, but i leave python for C++ (i've lost motivation for python
# C++ is just very cool and fast, even though it's hard)

pygame.mixer.init()
music_obj = music_class()

# pick a number randomly and choose a music using the number, there's only 4 music
# all the audio are OST from the game "Nameless cat"(it's a really good pixel game, have a try!)


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

if __name__ == '__main__':

    morpion_game = Morpion()
    morpion_game.run()
