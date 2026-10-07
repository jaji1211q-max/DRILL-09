from pathlib import Path

from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)


def handle_events():
    global running

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


try:
    tuk_ground = load_image(str(Path(__file__).resolve().parent / "TUK_GROUND.png"))
    character = load_image(str(Path(__file__).resolve().parent / "animation_sheet.png"))
    running = True
    frame = 0
    x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

    while running:
        handle_events()
        if running:
            x = min(x + 2, TUK_WIDTH - 50)
            frame = (frame + 1) % 8
            clear_canvas()
            tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            delay(0.005)
finally:
    close_canvas()