from pico2d import *

open_canvas()

character = load_image('ghost.png')
demon = load_image('demon_attack.png')

size = 32
frame = 0
stopSecond = 0.1

def idle():
    global frame
    for i in range(5):
        frame = 0
        for spriteLength in range(2):
            clear_canvas()
            character.clip_draw(frame * size, size * 8, size, size, 400, 300, 500, 500)
            update_canvas()
            frame = (frame + 1) % 2
            delay(0.4)
        delay(0.5)
    delay(stopSecond)
    pass

def walk():
    global frame
    for i in range(5):
        frame = 0
        for spriteLength in range(8):
            clear_canvas()
            character.clip_draw(frame * size, size * 5, size, size, 400, 300, 500, 500)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)
        delay(0.5)
    delay(stopSecond)

def jump():
    global frame
    for i in range(5):
        frame = 0
        for spriteLength in range(8):
            clear_canvas()
            character.clip_draw(frame * size, size * 3, size, size, 400, 300, 500, 500)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)
        delay(0.5)
    delay(stopSecond)
    pass

def attack():
    global frame
    for i in range(5):
        frame = 0
        for spriteLength in range(8):
            clear_canvas()
            character.clip_draw(frame * size, 0, size, size, 400, 300, 500, 500)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)
        delay(0.5)
    delay(stopSecond)

def die():
    global frame
    for i in range(5):
        frame = 0
        for j in range(8):
            clear_canvas()
<<<<<<< HEAD
            character.clip_draw(frame * size, size * 1, size, size, 400, 300, 500, 500)
=======
            clip = [1 + 0.1 * n for n in range(8)]
            character.clip_draw(frame * size, size, size, int(size / clip[j]) , 400, int(300/clip[j]), 500, int(500 / clip[j]))
>>>>>>> 9b3be5d (die 애니메이션에서 frame이 1 올라갈 때마다 프레임 크기를 조금씩 줄이게 변경)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)
        delay(0.5)
    delay(stopSecond)

while True:
    idle()
    walk()
    jump()
    attack()
    die()



close_canvas()

