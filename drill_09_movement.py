from pathlib import Path

from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
CHARACTER_HALF_WIDTH = 50
MOVE_SPEED = 400
open_canvas(TUK_WIDTH, TUK_HEIGHT)


def handle_events():
    global running, right_pressed, left_pressed, facing_right

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            right_pressed = True
            facing_right = True
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            right_pressed = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            left_pressed = True
            facing_right = False
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            left_pressed = False


try:
    tuk_ground = load_image(str(Path(__file__).resolve().parent / "TUK_GROUND.png"))
    character = load_image(str(Path(__file__).resolve().parent / "animation_sheet.png"))
    running = True
    right_pressed = False
    left_pressed = False
    facing_right = True
    frame = 0
    x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
    last_time = get_time()

    while running:
        handle_events()
        if running:
            current_time = get_time()
            delta_time = current_time - last_time
            last_time = current_time
            if right_pressed:
                x = min(x + MOVE_SPEED * delta_time, TUK_WIDTH - CHARACTER_HALF_WIDTH)
                frame = (frame + 1) % 8
                sprite_y = 100 if facing_right else 0
            elif left_pressed:
                x = max(x - MOVE_SPEED * delta_time, CHARACTER_HALF_WIDTH)
                frame = (frame + 1) % 8
                sprite_y = 100 if facing_right else 0
            else:
                frame = 0
                sprite_y = 300 if facing_right else 200
            clear_canvas()
            tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
            character.clip_draw(frame * 100, sprite_y, 100, 100, x, y)
            update_canvas()
            delay(0.005)
finally:
    close_canvas()