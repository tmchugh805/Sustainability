import random
import pandas as pd
import pygame
from utils import draw, Bin, Waste, Item, Score



def main():
    run = True
    file_name = 'Waste_List.csv'
    df = pd.read_csv(file_name)
    i = random.choice(range(len(df)))

    binheight = 450

    # load images
    LAB = Item("images/lab.jpg").load_image(800)
    WASTE = Waste("images/" + df.Image[i], df.Waste[i], df.Bin[i], df.Biohazard[i], df.Sharp[i],
                  df.Toxic[i])
    WASTE_IMAGE = WASTE.load_image(50)
    BinArray = []
    BinArray.append(Bin(item_path="images/Bin.png", position=(0, 300), bin_type="Autoclave"))
    BinArray.append(Bin(item_path="images/Toxic.png", position=(100, 300), bin_type="Yellow"))
    BinArray.append(Bin(item_path="images/Bin.png", position=(200, 300), bin_type="Glass"))
    BinArray.append(Bin(item_path="images/Bin.png", position=(300, 300), bin_type="Sharps"))
    BinArray.append(Bin(item_path="images/Bin.png", position=(400, 300), bin_type="General"))
    BinArray.append(Bin(item_path="images/Recycle.png", position=(500, 300), bin_type="Recycling"))
    BinArray.append(Bin(item_path="images/Cytotoxic.png", position=(600, 300), bin_type="Cytotoxic"))
    BinArray.append(Bin(item_path="images/Bin.png", position=(700, 300), bin_type="Other"))

    images = [(LAB, (0, 0)), (BinArray[0].load_image(75), (0, binheight)), (BinArray[1].load_image(75), (100, binheight)),
              (BinArray[2].load_image(75), (200, binheight)),
              (BinArray[3].load_image(75), (300, binheight)), (BinArray[4].load_image(75), (400, binheight)),
              (BinArray[5].load_image(75), (500, binheight)),
              (BinArray[6].load_image(75), (600, binheight)), (BinArray[7].load_image(75), (700, binheight))]
    scoreboard.reset()

    ## set initial image position
    waste_x = random.randrange(0, WIDTH)
    waste_y = 0
    move_right = False
    move_left = False
    move_down = False
    count = 0
    x_change = 0
    MAX_x_SPEED = 10
    y_change = 1


    while run:
        clock.tick(FPS)  # keep image at FPS 60 on all devices
        draw(WIN, images)  # draw all static images
        WIN.blit(WASTE_IMAGE, (waste_x, waste_y))  # draw image of waste
        font = pygame.font.SysFont("calibri", 20, bold=True, italic=False)
        WIN.blit(font.render(df.Waste[i], True, (0, 0, 0)), (50, 10))  # display waste name on screen
        scoreboard.display(WIN)
        pygame.display.update()  # show your drawings on screen



        if count == 10:  # if user presses clicks X
            break


        for event in pygame.event.get():  # loop through all events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: # if user presses right arrow key
                    move_right = True
                    x_change = 2  # initial speed
                if event.key == pygame.K_LEFT: # if user presses left arrow key
                    move_left = True
                    x_change = -2  # initial speed
                if event.key == pygame.K_DOWN: # if user presses left arrow key
                    move_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT: # if user releases right arrow key
                    move_right = False
                    x_change = 0  # stop waste
                if event.key == pygame.K_LEFT: # if user releases left arrow key
                    move_left = False
                    x_change = 0  # stop waste
                if event.key == pygame.K_DOWN: # if user presses left arrow key
                    move_down = False
                    y_change = 1  # reset step falling speed
            elif event.type == pygame.QUIT: # if user presses clicks X
                run = False
                break
        if move_right:
            x_accel = 0.2  # right acceleration
            x_change += x_accel
        if move_left:
            x_accel = -0.2  # left acceleration
            x_change += x_accel
        if move_down:
            y_accel = 0.5  # down acceleration
            y_change += y_accel

        if abs(x_change) >= MAX_x_SPEED:  # limit speed below maximal speed
            if x_change > 0:
                x_change = MAX_x_SPEED
            else:
                x_change = - MAX_x_SPEED

        waste_x += x_change
        waste_y += y_change  # cause object to fall

        # for event in pygame.event.get():  # loop through all events
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_RIGHT: # if user presses right arrow key
        #             move_right = True
        #         if event.key == pygame.K_LEFT: # if user presses left arrow key
        #             move_left = True
        #     elif event.type == pygame.KEYUP:
        #         if event.key == pygame.K_RIGHT: # if user releases right arrow key
        #             move_right = False
        #         if event.key == pygame.K_LEFT: # if user releases left arrow key
        #             move_left = False
        #     elif event.type == pygame.QUIT: # if user presses clicks X
        #         run = False
        #         break
        # if move_right:
        #     waste_x += 1  # move object to the right
        # if move_left:
        #     waste_x -= 1  # move object to the left
        # waste_y += WASTE_SPEED # cause object to fall

        if waste_y > HEIGHT:  # if object moves off screen
            correct_bin = WASTE.get_bintype()
            actual_bin = which_bin(waste_x, BinArray)
            if correct_bin == actual_bin:
                scoreboard.add()
            waste_x = random.randrange(0, WIDTH)  # new object falls from different x position on screen
            waste_y = -25  # bring new object at different position
            i = random.choice(range(len(df)))
            WASTE = Waste("images/" + df.Image[i], df.Waste[i], df.Bin[i], df.Biohazard[i], df.Sharp[i],
                          df.Toxic[i])
            WASTE_IMAGE = WASTE.load_image(50)  # select random waste
            count = count + 1


def which_bin(waste_x, binarray):
    for bin in binarray:
        bin_position = bin.get_position()
        x_position = bin_position[0]
        if x_position <= waste_x < (x_position + 100):
            return bin.get_bintype()
    return "Null"


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

            width = 100
            height = 50

            xposition = 600
            ypostiongreen = 350
            ypostionred = 400

            if xposition + width > mouse[0] > xposition and ypostiongreen + height > mouse[1] > ypostiongreen:
                pygame.draw.rect(screen, bright_green, (xposition, ypostiongreen, width, height))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    main()
            else:
                pygame.draw.rect(screen, green, (xposition, ypostiongreen, width, height))

            if xposition + width > mouse[0] > xposition and ypostionred + 75 > mouse[1] > ypostionred:
                pygame.draw.rect(screen, bright_red, (xposition, ypostionred, width, height))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
                    break
            else:
                pygame.draw.rect(screen, red, (xposition, ypostionred, width, height))

           # screen.blit(font_large.render("Waste Disposal Game", True, (255, 255, 255)), (325, 50))
            screen.blit(font.render("Play", True, (0, 0, 0)), ((xposition+17), (ypostiongreen+30)))
            screen.blit(font.render("Quit", True, (0, 0, 0)), ((xposition+17), (ypostionred+30)))
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
WIN = pygame.display.set_mode((800, 550), pygame.RESIZABLE)

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
scoreboard = Score(0, 700, 10)

main_menu(WIN, clock, FPS, scoreboard)
