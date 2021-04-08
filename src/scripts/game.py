import pygame, os, json, pyautogui, sys, time

from .modules.input import Input
from .modules.notification import Notification_Handler
from .modules.language import Language_Handler
from .modules.colors import Color_Handler
from .modules.fonts import Font_Handler
from .modules.sound import Sound_Handler
from .typemania.typemania import typemania

from .options import options

class Game:
    main_screen = pygame.display.set_mode((1920, 1080))
    main_surface = pygame.Surface((1920, 1080))

    game_speed = 1
    clock = pygame.time.Clock()

    running = True
    title = "Game"

    current_assetpack = "main"

    display_width, display_height = pyautogui.size()

    def stop(self):
        self.running = False

    def change_title(self, title):
        self.title = title
        pygame.display.set_caption(title)

    def __init__(self):
        self.input = Input()
        self.notification_handler = Notification_Handler(self)
        self.language_handler = Language_Handler(self)
        self.color_handler = Color_Handler(self)
        self.font_handler = Font_Handler(self)
        self.sound_handler = Sound_Handler(self)

        self.typemania = typemania(self)

        self.display_width, self.display_height = pyautogui.size()

        self.scene_options = options(self)

        self.show_debug = False

        self.previous_time = time.time()

        with open(os.path.join("src", "properties.json"), "r") as file:
            self.properties = json.load(file)

        self.change_title(self.properties["id"])
        icon = pygame.image.load(os.path.join("src", "resources", self.current_assetpack, "assets", "icon.png"))
        pygame.display.set_icon(icon)

    def initialize(self):
        self.notification_handler.send("Successful Start", "Game started succesfully on version " + self.properties["version"])
        self.change_title(self.properties["id"])
        self.input.input_state = "game"

    def begin_update(self):

        # Calculate Delta Time
        now = time.time()
        self.delta_time = now - self.previous_time
        self.previous_time = now

        self.input.any_key_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            if event.type == pygame.KEYDOWN:
                self.input.any_key_pressed = True

    def update(self):
        self.scene_options.update()

    def end_update(self):
        self.notification_handler.update()

        self.input.check_keys()

    def render(self):
        self.scene_options.render()

        self.notification_handler.render()

        copyright_text = self.font_handler.get_font("default_15").render("willmexe © 2021", True, (self.color_handler.get_color_rgb("typemania.text")))
        self.main_surface.blit(copyright_text, (self.display_width / 2 - copyright_text.get_width() / 2, self.display_height - self.font_handler.get_font_size("default_15") - 10))

    def main_loop_final(self, update_time, render_time):
        if self.scene_options.show_fps == True:
            self.scene_options.fps_module.draw_stats(update_time, render_time)

        surf = self.main_surface
        if self.main_screen.get_width() != self.main_surface.get_width():
            if self.main_screen.get_height() != self.main_surface.get_height():
                surf = pygame.transform.scale(self.main_surface, (self.main_screen.get_width(), self.main_screen.get_height()))
        self.main_screen.blit(surf, (0, 0))
        pygame.display.update()
        self.clock.tick(60)