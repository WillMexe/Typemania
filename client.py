import pygame, time
from src.scripts.game import Game

game = Game()

game.initialize()

game.typemania.switch_scene("main_screen")

def begin_update():
    game.begin_update()

def update():
    game.update()

    if game.typemania.current_scene == "main_screen":
        game.typemania.main_screen_scene.update()
    elif game.typemania.current_scene == "pack_selection":
        game.typemania.pack_selection_scene.update()
    elif game.typemania.current_scene == "typing_test":
        game.typemania.typing_test_scene.update()
    elif game.typemania.current_scene == "result_screen":
        game.typemania.result_screen_scene.update()

def end_update():
    game.end_update()

def render():
    game.main_surface.fill(game.color_handler.get_color_rgb("typemania.background")) 

    if game.typemania.current_scene == "main_screen":
        game.typemania.main_screen_scene.render()
    elif game.typemania.current_scene == "pack_selection":
        game.typemania.pack_selection_scene.render()
    if game.typemania.current_scene == "typing_test":
        game.typemania.typing_test_scene.render()
    elif game.typemania.current_scene == "result_screen":
        game.typemania.result_screen_scene.render()

    game.render()

def stop():
    game.typemania.stop()

while game.running:
    update_start_time = time.time()
    begin_update()

    update()

    end_update()
    update_end_time = time.time()

    render_start_time = time.time()
    render()
    render_end_time = time.time()

    game.main_loop_final(update_end_time - update_start_time, render_end_time - render_start_time)

stop()
pygame.quit()