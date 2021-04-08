import pygame, math

class fps:

    def __init__(self, game):
        self.game = game

        self.update_filler_text = self.game.font_handler.get_font("default_18").render("Update:          Fps (           ms)", True, self.game.color_handler.get_color_rgb("options.text"))
        self.render_filler_text = self.game.font_handler.get_font("default_18").render("Render:          Fps (           ms)", True, self.game.color_handler.get_color_rgb("options.text"))
        self.total_filler_text = self.game.font_handler.get_font("default_18").render( "Total   :          Fps (           ms)", True, self.game.color_handler.get_color_rgb("options.text"))

    def draw_stats(self, update_time, draw_time):
        s = pygame.Surface((260, 90), pygame.SRCALPHA)
        pygame.draw.rect(s, self.game.color_handler.get_color_rgb("options.background"), ((0, 0), (270, 100)), False, 10)
        s.set_alpha(128)
        self.game.main_surface.blit(s, (self.game.display_width - 260, self.game.display_height - 90))

        update_fps_text = self.game.font_handler.get_font("default_18").render(str(1 / max(update_time, 0.0001)).split(".")[0], True, self.game.color_handler.get_color_rgb("options.text"))
        render_fps_text = self.game.font_handler.get_font("default_18").render(str(1 / max(draw_time, 0.0001)).split(".")[0], True, self.game.color_handler.get_color_rgb("options.text"))
        total_fps_text = self.game.font_handler.get_font("default_18").render(str(1 / max(draw_time + update_time, 0.0001)).split(".")[0], True, self.game.color_handler.get_color_rgb("options.text"))

        update_time_text = self.game.font_handler.get_font("default_18").render(str(update_time * 1000)[0: 5], True, self.game.color_handler.get_color_rgb("options.text"))
        render_time_text = self.game.font_handler.get_font("default_18").render(str(draw_time * 1000)[0: 5], True, self.game.color_handler.get_color_rgb("options.text"))
        total_time_text = self.game.font_handler.get_font("default_18").render(str((draw_time + update_time) * 1000)[0: 5], True, self.game.color_handler.get_color_rgb("options.text"))

        self.game.main_surface.blit(self.update_filler_text, (self.game.display_width - 250, self.game.display_height - update_fps_text.get_height() - 10))
        self.game.main_surface.blit(self.render_filler_text, (self.game.display_width - 250, self.game.display_height - render_fps_text.get_height() * 2 - 10))
        self.game.main_surface.blit(self.total_filler_text, (self.game.display_width - 250, self.game.display_height - total_fps_text.get_height() * 3 - 10))

        self.game.main_surface.blit(update_fps_text, (self.game.display_width - 182, self.game.display_height - update_fps_text.get_height() - 10))
        self.game.main_surface.blit(render_fps_text, (self.game.display_width - 182, self.game.display_height - render_fps_text.get_height() * 2 - 10))
        self.game.main_surface.blit(total_fps_text, (self.game.display_width - 182, self.game.display_height - total_fps_text.get_height() * 3 - 10))

        self.game.main_surface.blit(update_time_text, (self.game.display_width - 90, self.game.display_height - update_time_text.get_height() - 10))
        self.game.main_surface.blit(render_time_text, (self.game.display_width - 90, self.game.display_height - render_time_text.get_height() * 2 - 10))
        self.game.main_surface.blit(total_time_text, (self.game.display_width - 90, self.game.display_height - total_time_text.get_height() * 3 - 10))