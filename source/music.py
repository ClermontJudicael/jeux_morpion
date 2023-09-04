import pygame
import os

# fontion pour les musiques de fond


class music_class:

    def play_music1(self):
        self.sound_effect = pygame.mixer.Sound(
            "./music/background_sound.wav")
        self.sound_effect.set_volume(0.5)
        self.sound_effect.play(-1)

    def play_music2(self):
        self.sound_effect = pygame.mixer.Sound(
            "./music/Nameless_Cat_OST_Dusk.wav")
        self.sound_effect.set_volume(0.5)
        self.sound_effect.play(-1)

    def play_music3(self):
        self.sound_effect = pygame.mixer.Sound(
            "./music/Nameless_Cat_OST_Memory.wav")
        self.sound_effect.set_volume(0.5)
        self.sound_effect.play(-1)

    def play_music4(self):
        self.sound_effect = pygame.mixer.Sound(
            "./music/Nameless_Cat_2018_Trailer.wav")
        self.sound_effect.set_volume(0.5)
        self.sound_effect.play(-1)

    def play_soundO(self):  # pour O
        self.sound_effect = pygame.mixer.Sound(
            "./music/O.wav")
        self.sound_effect.set_volume(9)
        self.sound_effect.play()

    def play_soundX(self):  # pour X
        self.sound_effect = pygame.mixer.Sound(
            "./music/X.wav")
        self.sound_effect.set_volume(9)
        self.sound_effect.play()

        # fontion pour l'audio des autres boutons

    def clic(self):
        self.sound_effect = pygame.mixer.Sound(
            "./music/button_on_clic.wav")
        self.sound_effect.set_volume(9)
        self.sound_effect.play()

        # fontion pour l'audio quand le joueur gagne

    def win(self):
        self.sound_effect = pygame.mixer.Sound(
            "./music/Winning_Sound_Effect.wav")
        self.sound_effect.set_volume(9)
        self.sound_effect.play()

        # fonction pour l'audio quand c'est match nul

    def loose(self):
        self.sound_effect = pygame.mixer.Sound(
            "./music/Fail_sound_effect.wav")
        self.sound_effect.set_volume(0.2)
        self.sound_effect.play()
