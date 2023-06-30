import pygame

# fontion pour les musiques de fond


class music_class:

    def play_music1(self):
        self.sound_effect = pygame.mixer.Sound(
            "C:\\Users\\users\\Desktop\\tic_tac\\music\\background_sound.wav")
        self.sound_effect.set_volume(0.5)
        self.sound_effect.play(-1)  # -1 plays the music in a loop

    def play_music2(self):
        self.sound_effect = pygame.mixer.Sound(
            "C:\\Users\\users\\Desktop\\tic_tac\\music\\Nameless_Cat_OST_Dusk.wav")
        self.sound_effect.set_volume(0.5)
        self.sound_effect.play(-1)  # -1 plays the music in a loop

    def play_music3(self):
        self.sound_effect = pygame.mixer.Sound(
            "C:\\Users\\users\\Desktop\\tic_tac\\music\\Nameless_Cat_OST_Memory.wav")
        self.sound_effect.set_volume(0.5)
        self.sound_effect.play(-1)  # -1 plays the music in a loop

    def play_music4(self):
        self.sound_effect = pygame.mixer.Sound(
            "C:\\Users\\users\\Desktop\\tic_tac\\music\\Nameless_Cat_2018_Trailer.wav")
        self.sound_effect.set_volume(0.5)
        self.sound_effect.play(-1)  # -1 plays the music in a loop

        # fontion pour les audio X et O

    def play_soundO(self):
        self.sound_effect = pygame.mixer.Sound(
            "C:\\Users\\users\\Desktop\\tic_tac\\music\\O.wav")
        self.sound_effect.set_volume(9)
        self.sound_effect.play()

    def play_soundX(self):
        self.sound_effect = pygame.mixer.Sound(
            "C:\\Users\\users\\Desktop\\tic_tac\\music\\X.wav")
        self.sound_effect.set_volume(9)
        self.sound_effect.play()

        # fontion pour l'audio des autres boutons

    def clic(self):
        self.sound_effect = pygame.mixer.Sound(
            "C:\\Users\\users\\Desktop\\tic_tac\\music\\button_on_clic.wav")
        self.sound_effect.set_volume(9)
        self.sound_effect.play()

        # fontion pour l'audio quand le joueur gagne

    def win(self):
        self.sound_effect = pygame.mixer.Sound(
            "C:\\Users\\users\\Desktop\\tic_tac\\music\\Winning_Sound_Effect.wav")
        self.sound_effect.set_volume(9)
        self.sound_effect.play()

        # fonction pour k'audio quand c'est match nul

    def loose(self):
        self.sound_effect = pygame.mixer.Sound(
            "C:\\Users\\users\\Desktop\\tic_tac\\music\\Fail_sound_effect.wav")
        self.sound_effect.set_volume(0.2)
        self.sound_effect.play()

    # def clicX(self):
