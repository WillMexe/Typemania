import json, os, pygame
pygame.font.init()

class Font_Handler:
    
    fonts = {
        "Ariel": {
            "file": pygame.font.SysFont('Ariel', 35),
            "size": 35
        }
    }

    def load_font(self, font, size, name=""):
        font_file = pygame.font.Font(os.path.join("src", "resources", self.game.current_assetpack, "assets", "fonts", font + ".ttf"), size)
        if name == "":
            self.fonts[font] = {
                "file": font_file,
                "size": size
            }
        else:
            self.fonts[name] = {
                "file": font_file,
                "size": size
            }

    def get_font(self, font, bold=False, italic=False, underline=False):
        if font in self.fonts:
            font_file = self.fonts[font]["file"]
                
            font_file.bold = bold
            font_file.italic = italic
            font_file.underline = underline
            
            return font_file
        else:
            return self.fonts[list(self.fonts.keys())[0]]["file"]

    def get_font_size(self, font):
        if font in self.fonts:
            return self.fonts[font]["size"]
        else:
            return self.fonts[list(self.fonts.keys())[0]]["size"]

    def __init__(self, game):
        self.game = game

        self.load_font("default", 40)
        self.load_font("default", 18, "default_18")
        self.load_font("default", 15, "default_15")