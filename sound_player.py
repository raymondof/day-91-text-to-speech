import pygame

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()

    def set_path(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    def pause_sound(self):
        pygame.mixer.music.pause()


    def play_sound(self):
        pygame.mixer.music.unpause()
