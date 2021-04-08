import pygame
from .modules.options.fps import fps

class options:

    def __init__(self, game):
        self.game = game

        self.open = False

        self.show_fps = False

        self.fps_module = fps(game)

        self.menu_id = 0

        self.marker_target_y = 200 + (self.menu_id * 70)
        self.marker_y = self.marker_target_y

        self.marker_x = 90

        self.show_fps_text_surface = self.game.font_handler.get_font("default").render(self.game.language_handler.translatable_text("typemania.options.show_fps") + ": " + str(self.show_fps), True, (self.game.color_handler.get_color_rgb("typemania.text")))
        self.reset_save_text_surface = self.game.font_handler.get_font("default").render(self.game.language_handler.translatable_text("typemania.options.reset_save"), True, (self.game.color_handler.get_color_rgb("typemania.text")))

        self.marker_target_width = self.show_fps_text_surface.get_width() + 20
        self.marker_width = self.marker_target_width

        self.bg_target_x = -1000
        self.bg_x = self.bg_target_x

    def update(self):
        self.bg_x += (self.bg_target_x - self.bg_x) / 10
        if self.open:
            self.bg_target_x = 5
            self.game.input.input_state = "options"
            if self.game.input.is_pressed("esc"):
                self.open = False

            if self.game.input.is_just_pressed("DOWN"):
                self.menu_id += 1
            if self.game.input.is_just_pressed("UP"):
                self.menu_id -= 1

            self.show_fps_text_surface = self.game.font_handler.get_font("default").render(self.game.language_handler.translatable_text("typemania.options.show_fps") + ": " + str(self.show_fps), True, (self.game.color_handler.get_color_rgb("typemania.text")))

            self.marker_target_y = 270 + (self.menu_id * 140) - 25
            self.marker_y += (self.marker_target_y - self.marker_y) / 8
            self.marker_width += (self.marker_target_width - self.marker_width) / 20

            if self.menu_id < 0:
                self.menu_id = 1
            if self.menu_id > 1:
                self.menu_id = 0

            if self.menu_id == 0:
                self.marker_target_width = self.show_fps_text_surface.get_width() + 20
            if self.menu_id == 1:
                self.marker_target_width = self.reset_save_text_surface.get_width() + 20

            if self.game.input.is_just_pressed("SPACE") or self.game.input.is_just_pressed("RETURN"):
                if self.menu_id == 0:
                    self.show_fps = not self.show_fps
                if self.menu_id == 1:
                    self.game.typemania.save_file = {"all_plays": []}
                    self.game.notification_handler.send("Save File Reset", "Typemania save file has been reset from the options menu.")
        
        else:
            self.game.input.input_state = "game"
            self.bg_target_x = -1000
        
        if self.game.input.is_pressed("ctrl") and self.game.input.is_just_pressed("o"):
            self.open = not self.open

    def render(self):
        pygame.draw.rect(self.game.main_surface, self.game.color_handler.get_color_rgb("options.background"), ((self.bg_x, 5), (500, self.game.display_height - 10)), False, 5)
 
        if self.open:
            pygame.draw.rect(self.game.main_surface, self.game.color_handler.get_color_rgb("typemania.marker"), ((self.marker_x, self.marker_y), (self.marker_width, 5)), False, 5)

            self.game.main_surface.blit(self.show_fps_text_surface, (100, 200))
            self.game.main_surface.blit(self.reset_save_text_surface, (100, 340))