from pico2d import *

open_canvas()

character = load_image('ghost.png')

size = 32
frame = 0
stopSecond = 0.1

def idle():
    global frame
    for i in range(5):
        for spriteLength in range(2):
            clear_canvas()
            character.clip_draw(frame * size, size * 8, size, size, 400, 300, 500, 500)
            update_canvas()
            frame = (frame + 1) % 4
            delay(0.2)
    delay(stopSecond)
    pass

def walk():
    global frame
    for i in range(5):
        for spriteLength in range(8):
            clear_canvas()
            character.clip_draw(frame * size, size * 5, size, size, 400, 300, 500, 500)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)
    delay(stopSecond)

def jump():
    global frame
    for i in range(5):
        for spriteLength in range(8):
            clear_canvas()
            character.clip_draw(frame * size, size * 3, size, size, 400, 300, 500, 500)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)
    delay(stopSecond)
    pass

def attack():
    global frame
    for i in range(5):
        for spriteLength in range(8):
            clear_canvas()
            character.clip_draw(frame * size, 0, size, size, 400, 300, 500, 500)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)
    delay(stopSecond)

def die():
    global frame
    for i in range(5):
        for spriteLength in range(8):
            clear_canvas()
            #여기 채우면 끝
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)
    delay(stopSecond)

while True:
    idle()
    walk()
    jump()
    attack()
    die()



close_canvas()

