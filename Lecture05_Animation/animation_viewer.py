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
        pass
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

