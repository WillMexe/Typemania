import json, os

class Language_Handler:
    current_language_id = "en_US"

    def __init__(self, game):
        self.game = game

        with open(os.path.join("src", "resources", self.game.current_assetpack, "data", "lang", self.current_language_id + ".json"), "r") as lang_file:
            self.lang_json = json.load(lang_file)
    
    def translatable_text(self, lang_file_link):
        if lang_file_link in self.lang_json:
            text = self.lang_json[lang_file_link]
            return text
        else:
            return lang_file_link
        
