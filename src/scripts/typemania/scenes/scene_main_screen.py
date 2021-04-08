import pygame, random
from colormap import hex2rgb
pygame.init()
pygame.font.init()

class main_screen:

    def __init__(self, game):
        self.game = game

        self.play_text_surface = self.game.font_handler.get_font("default").render(self.game.language_handler.translatable_text("typemania.main_screen.play"), True, (self.game.color_handler.get_color_rgb("typemania.text")))
        self.options_text_surface = self.game.font_handler.get_font("default").render(self.game.language_handler.translatable_text("typemania.main_screen.options"), True, (self.game.color_handler.get_color_rgb("typemania.text")))
        self.exit_text_surface = self.game.font_handler.get_font("default").render(self.game.language_handler.translatable_text("typemania.main_screen.exit"), True, (self.game.color_handler.get_color_rgb("typemania.text")))

        self.menu_id = 0

        self.marker_target_y = (self.game.display_height / 2) + (70 * self.menu_id) + 10
        self.marker_y = self.marker_target_y

        if self.menu_id == 0:
            self.marker_target_width = self.play_text_surface.get_width()
        if self.menu_id == 1:
            self.marker_target_width = self.options_text_surface.get_width()
        if self.menu_id == 2:
            self.marker_target_width = self.exit_text_surface.get_width()

        self.marker_target_x = (self.game.display_width / 2) - (self.marker_target_width / 2) - 10
        self.marker_target_width += 20

        self.marker_width = self.marker_target_width
        self.marker_x = self.marker_target_x

        self.marker_x = self.marker_target_x

    def update(self):

        if self.game.input.is_just_pressed("UP", "game"):
            self.menu_id -= 1
        if self.game.input.is_just_pressed("DOWN", "game"):
            self.menu_id += 1

        if self.game.input.is_just_pressed("SPACE", "game") or self.game.input.is_just_pressed("RETURN", "game"):
            if self.menu_id == 0:
                self.game.typemania.switch_scene("pack_selection")
                #self.game.typemania.start_quote(random.randint(0, len(self.game.typemania.quotes) - 1))
            if self.menu_id == 1:
                self.game.scene_options.open = True
            if self.menu_id == 2:
                self.game.stop()

        if self.menu_id < 0:
            self.menu_id = 2
        if self.menu_id > 2:
            self.menu_id = 0

        self.marker_target_y = (self.game.display_height / 2) + (70 * self.menu_id) + 10
        self.marker_y += (self.marker_target_y - self.marker_y) / 8

        self.marker_width += (self.marker_target_width - self.marker_width) / 10
        self.marker_x += (self.marker_target_x - self.marker_x) / 10

        if self.menu_id == 0:
            self.marker_target_width = self.play_text_surface.get_width()
        if self.menu_id == 1:
            self.marker_target_width = self.options_text_surface.get_width()
        if self.menu_id == 2:
            self.marker_target_width = self.exit_text_surface.get_width()
        
        self.marker_target_x = (self.game.display_width / 2) - (self.marker_target_width / 2) - 10
        self.marker_target_width += 20

    def render(self):

        pygame.draw.rect(self.game.main_surface, (self.game.color_handler.get_color_rgb("typemania.marker")), ((self.marker_x, self.marker_y), (self.marker_width, 5)), False, 5)

        self.game.main_surface.blit(self.play_text_surface, (self.game.display_width / 2 - self.play_text_surface.get_width() / 2, self.game.display_height / 2 - self.game.font_handler.get_font_size("default_42")))
        self.game.main_surface.blit(self.options_text_surface, (self.game.display_width / 2 - self.options_text_surface.get_width() / 2, self.game.display_height / 2 + self.game.font_handler.get_font_size("default_42")))
        self.game.main_surface.blit(self.exit_text_surface, (self.game.display_width / 2 - self.exit_text_surface.get_width() / 2, self.game.display_height / 2 + self.game.font_handler.get_font_size("default_42") * 3))