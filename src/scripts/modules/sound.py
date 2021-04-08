import pygame, os
pygame.mixer.init()

class Sound_Handler:

    sounds = {}

    def __init__(self, game):
        self.game = game

    def load_sound(self, sound_id, sound_file):
        self.sounds[sound_id] = {
            "file": pygame.mixer.Sound(os.path.join("src", "resources", self.game.current_assetpack, "assets", "sounds", sound_file + ".ogg"))
        }

    def play_sound(self, sound_id):
        self.sounds[sound_id]["file"].play()