import json, pygame, random, os
from .scenes.scene_main_screen import main_screen
from .scenes.scene_result_screen import result_screen
from .scenes.scene_type_test import typing_test
from .scenes.scene_pack_selection import pack_selection

pygame.mixer.init()

class typemania:

    def __init__(self, game):
        self.game = game

        self.typing_test_scene = typing_test(self.game)
        self.result_screen_scene = result_screen(self.game)
        self.main_screen_scene = main_screen(self.game)
        self.pack_selection_scene = pack_selection(self.game)

        self.game.sound_handler.load_sound("key_sound_0", "key_sound_0")
        self.game.sound_handler.load_sound("key_sound_1", "key_sound_1")
        self.game.sound_handler.load_sound("key_sound_2", "key_sound_2")
        self.game.sound_handler.load_sound("key_sound_3", "key_sound_3")

        if not os.path.exists(os.path.join("save_data", "typemania_save.json")):
            with open(os.path.join("save_data", "typemania_save.json"), "w") as file:
                file.write('{"all_plays": []}') 
        with open(os.path.join("save_data", "typemania_save.json"), "r") as file_save_file:
            self.save_file = json.load(file_save_file)

    quotes = [{'quote': 'The quick brown fox jumps over the lazy dog', 'author': 'The Boston Journal'},
              {'quote': 'I have no special talent. I am only passionately curious.', 'author': 'Albert Einstein'},
              {'quote': 'Dont count the days, make the days count.', 'author': 'Muhammad Ali'}]

    current_scene = ""

    clock = pygame.time.Clock()
    dt = 0

    def play_key_sound(self):
        random_int = random.randint(0, 3)
        self.game.sound_handler.play_sound("key_sound_" + str(random_int))

    def switch_scene(self, scene):
        self.current_scene = scene

    def start_quote(self, quote):
        self.typing_test_scene.type_this = self.quotes[quote]["quote"]
        self.typing_test_scene.quote = quote
        self.switch_scene("typing_test")

    def show_result_screen(self, quote, net_wpm, errors):
        self.result_screen_scene.quote = quote
        self.result_screen_scene.net_wpm = net_wpm
        self.result_screen_scene.errors = errors
        self.switch_scene("result_screen")

    def stop(self):
        with open(os.path.join("save_data", "typemania_save.json"), "w") as file:
            file.write(str(self.save_file).replace("'", '"'))