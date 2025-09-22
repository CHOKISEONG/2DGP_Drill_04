from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('ghost.png')
for i in range(5):
    clear_canvas()
    character.clip_draw(frame * size, 0, size, size, 400, 300, 300, 300)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
size = 32
# fill here
frame = 0
while True:
    for x in range(0, 800, 10):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * size, 0, size, size, x, 120, 150, 150)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
    for x in range(800, 0, -10):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_composite_draw(frame * size, 0, size, size, 0, 'h', x, 120, 150, 150)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)


close_canvas()

