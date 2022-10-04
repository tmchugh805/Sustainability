import random
import pandas as pd
import pygame
from utils import draw, Bin, Waste, Item, Score



def main():
    run = True
    file_name = 'Waste_List.csv'
    df = pd.read_csv(file_name)
    i = random.choice(range(len(df)))


    # load images
    LAB = Item("images/lab.jpg").load_image()
    WASTE = Waste("images/" + df.Image[i], df.Waste[i], df.Bin[i], df.Biohazard[i], df.Sharp[i], df.Toxic[i]).load_image(50)
    BIN1 = Bin(item_path="images/Bin.png", position=(0, 300), bin_type="images/Bin.png").load_image(75)
    BIN2 = Bin(item_path="images/Bin.png", position=(100, 300), bin_type="images/Bin.png").load_image(75)
    BIN3 = Bin(item_path="images/Bin.png", position=(200, 300), bin_type="images/Bin.png").load_image(75)
    BIN4 = Bin(item_path="images/Bin.png", position=(300, 300), bin_type="images/Bin.png").load_image(75)

    WASTE_SPEED = 1

    images = [(LAB, (0, 0)), (BIN1, (0, 300)), (BIN2, (100, 300)), (BIN3, (200, 300)), (BIN4, (300, 300))]
    scoreboard.reset()

    ## set initial image position
    waste_x = random.randrange(0, WIDTH)
    waste_y = 0
    move_right = False
    move_left = False
    count = 0

    while run:
        clock.tick(FPS)  # keep image at FPS 60 on all devices
        draw(WIN, images)  # draw all static images
        WIN.blit(WASTE, (waste_x, waste_y))  # draw image of waste
        scoreboard.display(WIN)
        pygame.display.update()  # show your drawings on screen

        if count == 10:  # if user presses clicks X
            break

        for event in pygame.event.get():  # loop through all events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: # if user presses right arrow key
                    move_right = True
                if event.key == pygame.K_LEFT: # if user presses left arrow key
                    move_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT: # if user releases right arrow key
                    move_right = False
                if event.key == pygame.K_LEFT: # if user releases left arrow key
                    move_left = False
            elif event.type == pygame.QUIT: # if user presses clicks X
                run = False
                break
        if move_right:
            waste_x += 1 # move object to the right
        if move_left:
            waste_x -= 1 # move object to the left
        waste_y += WASTE_SPEED # cause object to fall

        if waste_y > HEIGHT:  # if object moves off screen
            waste_x = random.randrange(0, WIDTH)  # new object falls from different x position on screen
            waste_y = -25  # bring new object at different position
            i = random.choice(range(len(df)))
            WASTE = Waste("images/" + df.Image[i], df.Waste[i], df.Bin[i], df.Biohazard[i], df.Sharp[i], df.Toxic[i]).load_image(50)  # select random waste
            scoreboard.add()
            count = count + 1


def main_menu(screen, clock, FPS, scoreboard):
    pygame.display.set_caption("Main Menu")
    run = True
    bright_green = (0, 255, 0)
    bright_red = (255, 0, 0)
    red = (200, 0, 0)
    green = (0, 200, 0)
    screen.fill((0, 0, 0))
    font_large = pygame.font.SysFont("calibri", 24, bold=True, italic=False)
    font = pygame.font.SysFont("calibri", 14, bold=True, italic=False)
    Finalscore = scoreboard.number

    # pygame.mixer.music.load('background_music_wav.wav')
    # pygame.mixer.music.play(-1)
    while run:

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                run = False

            if 400 + 100 > mouse[0] > 400 and 250 + 50 > mouse[1] > 250:
                pygame.draw.rect(screen, bright_green, (400, 250, 100, 50))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    main()
            else:
                pygame.draw.rect(screen, green, (400, 250, 100, 50))

            if 400 + 100 > mouse[0] > 400 and 300 + 75 > mouse[1] > 300:
                pygame.draw.rect(screen, bright_red, (400, 300, 100, 50))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
                    break
            else:
                pygame.draw.rect(screen, red, (400, 300, 100, 50))

            screen.blit(font_large.render("Waste Disposal Game", True, (255, 255, 255)), (325, 50))
            screen.blit(font.render("Play", True, (0, 0, 0)), (417, 285))
            screen.blit(font.render("Quit", True, (0, 0, 0)), (417, 330))
            screen.blit(font_large.render("Final Score: " + str(Finalscore), True, (0, 0, 0)), (150, 150))

        pygame.display.flip()
        clock.tick(FPS)


pygame.quit()

global WIN

# initialize mixer
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

LAB = pygame.image.load("images/lab.jpg")
WIDTH, HEIGHT = LAB.get_width(), LAB.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# set window name
pygame.display.set_caption("Sustainability Game!!!")

# play background music
pygame.mixer.music.load("sounds/lab_radio.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# set frame rate per second
FPS = 60

# code for main game
clock = pygame.time.Clock()
scoreboard = Score(0, 500, 10)

main_menu(WIN, clock, FPS, scoreboard)
