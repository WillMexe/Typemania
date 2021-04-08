import pygame, keyboard

class Input:

    input_state = "main"

    record_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                   "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                   "UP", "DOWN", "LEFT", "RIGHT", 
                   "SPACE", "CTRL", "SHIFT", "ALT", "RETURN", "ESCAPE", "TAB", "BACKSPACE"]

    def set_input_state(self, state):
        self.input_state = state

    def check_keys(self):
        for key in self.record_keys:
            exec("self.key_" + key + " = " + str(keyboard.is_pressed(key)))

    def __init__(self):
        self.check_keys()

        self.any_key_pressed = False

    def is_pressed(self, key, input_state=""):
        if input_state != "":
            return bool(keyboard.is_pressed(key) and pygame.mouse.get_focused() and input_state == self.input_state)
        else:
            return bool(keyboard.is_pressed(key) and pygame.mouse.get_focused())

    def is_just_pressed(self, key, input_state=""):
        exec("self.check_key = self.key_" + key)
        if input_state != "":
            return bool(self.check_key == False and keyboard.is_pressed(key) and input_state == self.input_state)
        else:
            return bool(self.check_key == False and keyboard.is_pressed(key))

    def is_any_key_pressed(self):
        return self.any_key_pressed