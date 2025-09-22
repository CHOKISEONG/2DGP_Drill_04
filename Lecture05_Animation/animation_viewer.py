from pico2d import *

open_canvas()

character = load_image('ghost.png')

size = 32
frame = 0

def idle():
    global frame
    for i in range(5):

        pass
    delay(1)
    pass

def walk():
    global frame

    delay(1)

def jump():
    global frame
    for i in range(5):
        pass
    delay(1)
    pass

def attack():
    global frame
    for i in range(5):
        clear_canvas()
        character.clip_draw(frame * size, 0, size, size, 400, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
    delay(1)

def die():
    global frame
    for i in range(5):
        pass
    delay(1)

while True:
    idle()
    walk()
    jump()
    attack()
    die()



close_canvas()

