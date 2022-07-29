import random

import pygame
from utils import scale_image


# initialize mixer
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()


# load images
LAB = pygame.image.load("images/lab.jpg")
GLOVE = scale_image(pygame.image.load("images/gloves.jpg"), 0.1)
BIN1 = scale_image(pygame.image.load("images/bin.jpg"), 0.1)
BIN2 = scale_image(pygame.image.load("images/bin.jpg"), 0.1)
BIN3 = scale_image(pygame.image.load("images/bin.jpg"), 0.1)
BIN4 = scale_image(pygame.image.load("images/bin.jpg"), 0.1)


# set window
WIDTH, HEIGHT = LAB.get_width(), LAB.get_height()
GLOVE_SPEED = 1
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# set window name
pygame.display.set_caption("Sustainability Game!!!")

# play background music
pygame.mixer.music.load("sounds/lab_radio.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# set frame rate per second
FPS = 60

def draw(win, images):
    for img, pos in images:
        win.blit(img, pos)


## set initial image position
glove_x = random.randrange(0, WIDTH)
glove_y = 0

# code for main game
run = True
clock = pygame.time.Clock()
images = [(LAB, (0,0)), (BIN1, (0, 300)), (BIN2, (100, 300)), (BIN3, (200, 300)), (BIN4, (300, 300))]


while run:
    clock.tick(FPS) # keep image at FPS 60 on all devices

    draw(WIN, images)
    WIN.blit(GLOVE, (glove_x, glove_y))

    pygame.display.update() # show your drawings on screen
    for event in pygame.event.get():  # loop through all events
        if event.type == pygame.QUIT:
            run = False
            break
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            glove_x += 10
        elif key[pygame.K_LEFT]:
            glove_x -= 10
    glove_y += GLOVE_SPEED
    if glove_y > HEIGHT:
        glove_x = random.randrange(0, WIDTH)
        glove_y = -25
        pygame.display.update()

pygame.quit()