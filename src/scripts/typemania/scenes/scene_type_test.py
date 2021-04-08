import pygame
from colormap import hex2rgb
pygame.init()
pygame.font.init()

class typing_test:

    def __init__(self, game):
        self.game = game

        self.marker_height = 5
        self.marker_width = 25
        self.marker_target_width = 25

        self.marker_x = 0
        self.marker_y = self.game.display_height / 2 - self.marker_height + 13

        self.marker_draw_x = self.marker_x
        self.marker_draw_y = self.marker_y

        self.type_this = ""
        self.typed_text = ""

        self.typed_entries = 0

        self.errors = 0
        self.wpm = 0
        
        self.done = False

        self.time = 1

        self.game.sound_handler.load_sound("error", "error")

        self.has_started = False

        self.next_letter = self.game.font_handler.get_font("default").render("H", True, self.game.color_handler.get_color_rgb("typemania.text"))

        self.black_cover_surf = pygame.Surface((1, 1), pygame.SRCALPHA)
        pygame.draw.rect(self.black_cover_surf, self.game.color_handler.get_color_rgb("options.background"), ((0, 0), (1, 1)))
        self.black_cover_surf.set_alpha(230)

        self.wpm = (self.typed_entries / 5) / (self.time / 60 / 60)
        self.net_wpm = self.wpm - (self.errors / max(int((self.time / 60) / 60), 1))

        self.net_wpm = max(self.net_wpm, 0)

        self.wpm_surface = self.game.font_handler.get_font("default").render("WPM: " + str(int(self.net_wpm)), True, self.game.color_handler.get_color_rgb("typemania.text"))

        self.text = self.game.font_handler.get_font("default").render(self.type_this, True, self.game.color_handler.get_color_rgb("typemania.text"))
        self.typed_text_surface = self.game.font_handler.get_font("default").render(self.typed_text, True, self.game.color_handler.get_color_rgb("typemania.dark_text"))
 
        self.y_offset_when_done = 0
        self.y_offset_when_done_target = 700

        self.game_done = False

    def reset(self):
        self.has_started = False
        self.typed_text = ""

        self.typed_entries = 0

        self.errors = 0
        self.wpm = 0
        
        self.done = False
        self.game_done = False

        self.time = 1
        self.y_offset_when_done = 0

    def update(self):
        self.time += 1
        if self.has_started and not self.game_done:

            if self.game.input.is_any_key_pressed():
                if len(self.type_this) != len(self.typed_text):
                    if self.type_this[len(self.typed_text)].lower() == " ":
                        exec('self.tmp_key = "SPACE"')
                    else:
                        exec('self.tmp_key = "' + self.type_this[len(self.typed_text)].lower() + '"')
                    if self.game.input.is_pressed(self.tmp_key, "game"):
                        self.game.typemania.play_key_sound()
                        self.typed_text += self.type_this[len(self.typed_text)]
                        if self.tmp_key != "SPACE":
                            self.typed_entries += 1
                    else:
                        if not self.game.input.is_pressed("shift"):
                            self.game.sound_handler.play_sound("error")
                            self.errors += 1

        else:
            if self.game.input.is_pressed(self.type_this[0]):
                self.has_started = True
                self.game.typemania.play_key_sound()
                if len(self.type_this) != len(self.typed_text):
                    self.typed_text += self.type_this[len(self.typed_text)]
                self.typed_entries += 1

        self.marker_draw_x += (self.marker_x - self.marker_draw_x) / 10
        self.marker_draw_y += (self.marker_y - self.marker_draw_y) / 10

        self.text = self.game.font_handler.get_font("default").render(self.type_this, True, self.game.color_handler.get_color_rgb("typemania.text"))
        self.typed_text_surface = self.game.font_handler.get_font("default").render(self.typed_text, True, self.game.color_handler.get_color_rgb("typemania.dark_text"))
        self.marker_x = self.game.display_width / 2 - self.text.get_width() / 2 + self.typed_text_surface.get_width()

        self.wpm_surface = self.game.font_handler.get_font("default").render("WPM: " + str(int(self.net_wpm)), True, self.game.color_handler.get_color_rgb("typemania.text"))
        
        if len(self.type_this) != len(self.typed_text):
            self.next_letter = self.game.font_handler.get_font("default").render(self.type_this[len(self.typed_text)], True, self.game.color_handler.get_color_rgb("typemania.text"))
        self.marker_target_width = self.next_letter.get_width()
        self.marker_width += (self.marker_target_width - self.marker_width) / 10

        if self.game_done:
            self.y_offset_when_done += (self.y_offset_when_done_target - self.y_offset_when_done) / 20

            if self.time >= 40:
                self.game.typemania.show_result_screen(self.quote, int(self.net_wpm), self.errors)
                self.reset()

        else:
            self.wpm = (self.typed_entries / 5) / (self.time / 60 / 60)
            self.net_wpm = self.wpm - (self.errors / max(int((self.time / 60) / 60), 1))

            self.net_wpm = max(self.net_wpm, 0)


            if len(self.type_this) == len(self.typed_text):
                self.game.typemania.save_file['all_plays'].append({
                    "quote": self.game.typemania.quotes[self.quote]["quote"],
                    "net_wpm": int(self.net_wpm),
                    "wpm": int(self.wpm),
                    "errors": self.errors
                })
                #self.game.typemania.show_result_screen(self.quote, int(net_wpm), self.errors)
                self.time = 0
                self.game_done = True
                #self.reset()

    def render(self):

        self.game.main_surface.blit(self.text, (self.game.display_width / 2 - self.text.get_width() / 2, self.game.display_height / 2 - 42 + self.y_offset_when_done))
        self.game.main_surface.blit(self.typed_text_surface, (self.game.display_width / 2 - self.text.get_width() / 2, self.game.display_height / 2 - 42 + self.y_offset_when_done))

        if self.has_started:
            pygame.draw.rect(self.game.main_surface, self.game.color_handler.get_color_rgb("typemania.marker"), ((self.marker_draw_x, self.marker_draw_y + self.y_offset_when_done), (self.marker_width, self.marker_height)), False, 5)

        self.game.main_surface.blit(self.wpm_surface, (self.game.display_width / 2 - self.text.get_width() / 2,  self.game.display_height / 2 - 126 + self.y_offset_when_done))

        if not self.has_started:
            self.game.main_surface.blit(pygame.transform.scale(self.black_cover_surf, (self.game.main_surface.get_width(), self.game.main_surface.get_height())), (0, 0))

            letter = self.type_this[0]
            if letter == 'I':
                letter = letter.lower()
            press_x_to_start = self.game.font_handler.get_font("default").render("Press '" + letter + "' to start", True, self.game.color_handler.get_color_rgb("typemania.text"))
            self.game.main_surface.blit(press_x_to_start, (self.game.display_width / 2 - press_x_to_start.get_width() / 2, 200))