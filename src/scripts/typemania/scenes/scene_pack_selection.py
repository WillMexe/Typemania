import pygame, random, os, json
from colormap import hex2rgb
pygame.init()
pygame.font.init()

class pack_selection:

    def __init__(self, game):
        self.game = game

        self.menu_id = 0

        quote_packs = os.listdir(os.path.join('src', 'resources', self.game.current_assetpack, 'data', 'quote_packs'))
        fixed_quote_packs = []

        for i in quote_packs:
            with open(os.path.join('src', 'resources', self.game.current_assetpack, 'data', 'quote_packs', i)) as file:
                fixed_quote_packs.append(json.load(file))

        self.quote_packs = fixed_quote_packs

        self.quote_pack_target_y = []
        self.quote_pack_y = []
        for i in range(len(self.quote_packs)):
            self.quote_pack_target_y.append(self.game.display_height / 2 - ((i - self.menu_id) * 70))
            self.quote_pack_y.append(self.game.display_height / 2 - ((i - self.menu_id) * 70))

        self.marker_target_width = 0
        self.marker_width = self.marker_target_width

        self.marker_target_x = self.game.display_width / 2
        self.marker_x = self.marker_target_x
        self.marker_y = self.game.display_height / 2 + 50

    def update(self):
        if self.game.input.is_just_pressed("UP", "game"):
            self.menu_id += 1
        if self.game.input.is_just_pressed("DOWN", "game"):
            self.menu_id -= 1

        if self.game.input.is_just_pressed("RETURN", "game") or self.game.input.is_just_pressed("SPACE", "game"):
            self.game.typemania.quotes = self.quote_packs[self.menu_id]["quotes"]
            self.game.typemania.start_quote(random.randint(0, len(self.game.typemania.quotes) - 1))

        if self.menu_id < 0:
            self.menu_id = len(self.quote_packs) - 1
        if self.menu_id > len(self.quote_packs) - 1:
            self.menu_id = 0

        for i in range(len(self.quote_packs)):
            self.quote_pack_target_y[i] = self.game.display_height / 2 - ((i - self.menu_id) * 70)
            self.quote_pack_y[i] += (self.quote_pack_target_y[i] - self.quote_pack_y[i]) / 10

        self.marker_width += (self.marker_target_width - self.marker_width) / 10
        self.marker_x += (self.marker_target_x - self.marker_x) / 10

    def render(self):

        pygame.draw.rect(self.game.main_surface, (self.game.color_handler.get_color_rgb("typemania.marker")), ((self.marker_x, self.marker_y), (self.marker_width, 5)), False, 5)

        for index, quote_pack in enumerate(self.quote_packs):
            text_surface = self.game.font_handler.get_font("default").render(quote_pack['display_name'], True, (self.game.color_handler.get_color_rgb("typemania.text")))
            if self.menu_id - index == 0:
                self.marker_target_width = text_surface.get_width() + 20
                self.marker_target_x = self.game.display_width / 2 - text_surface.get_width() / 2 - 10
            else:
                text_surface.set_alpha(256 / (abs(self.menu_id - index) * 1))

            self.game.main_surface.blit(text_surface, (self.game.display_width / 2 - text_surface.get_width() / 2, self.quote_pack_y[index]))