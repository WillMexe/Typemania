import pygame
from pygame import display

class Notification_Handler:

    notifications = []

    def __init__(self, game):
        self.game = game

    def send(self, title, message):
        print("[" + title + "] " + message)
        self.notifications.append({"title": title, "message": message, "time": 300})

    def render(self):
        height = 0
        last_end_y = 22

        for index, notification in enumerate(self.notifications):
            display_text = []
            current = ""
            message = notification["message"].split(" ")
            for index, word in enumerate(message):
                if current != "":
                    current += " " + word
                else:
                    current += word
                if index < len(message) - 1:
                    if len(current + message[index + 1]) > 30:
                        display_text.append(current)
                        current = ""
                
            display_text.append(current)

            height = 32 + (15 * len(display_text))
            pygame.draw.rect(self.game.main_surface, self.game.color_handler.get_color_rgb("notification.border"), ((self.game.main_surface.get_width() - 250, last_end_y), (230, height)), False, 10)
            pygame.draw.rect(self.game.main_surface, self.game.color_handler.get_color_rgb("notification.fill"), ((self.game.main_surface.get_width() - 246, last_end_y + 4), (222, height - 8)), False, 10)

            title_surface = self.game.font_handler.get_font("default_18", bold=True).render(notification["title"], True, self.game.color_handler.get_color_rgb("notification.text"))
            self.game.main_surface.blit(title_surface, (self.game.main_surface.get_width() - 241,  last_end_y + 2))

            for i, notif in enumerate(display_text):
                title_surface = self.game.font_handler.get_font("default_15").render(notif, True, self.game.color_handler.get_color_rgb("notification.text"))
                self.game.main_surface.blit(title_surface, (self.game.main_surface.get_width() - 241, last_end_y + (i * 14) + 20))

            last_end_y = height + 20 + last_end_y

    def update(self):
        new_notif = self.notifications.copy()
        for index, notification in enumerate(self.notifications):
            self.notifications[index]["time"] -= 1
            if self.notifications[index]["time"] <= 0:
                new_notif.pop(new_notif.index(self.notifications[index]))
        self.notifications = new_notif