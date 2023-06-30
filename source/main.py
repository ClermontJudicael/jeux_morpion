from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont
from music import music_class
from customtkinter import *
import pygame
import random
from function import Morpion

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

if __name__ == '__main__':

    morpion_game = Morpion()
    morpion_game.run()
