import random
import pandas as pd
import pygame
from pygame import VIDEORESIZE, QUIT, HWSURFACE, DOUBLEBUF, RESIZABLE

from utils import draw, Bin, Waste, Item, Score




def main():

    width = WIN.get_width()
    height = WIN.get_height()
    scoreboard.setposition(0.8*width,0.05*height)
    bonusscoreboard.setposition(0.8*width, 0.1*height)
    run = True
    file_name = 'Waste_List.csv'
    df = pd.read_csv(file_name)
    choicearray = list(range(0, len(df) - 1))
    random.shuffle(choicearray)
    count = 0
    i = choicearray[count]

    binheight = 450 * width / 800

    # load images
    LAB = Item("images/labBlur.jpg").load_image(width)
    # Bacteria = Item("images/Live Bacteria.png").load_image(60)
    WASTE = Waste("images/" + df.Image[i], df.Waste[i], df.Bin[i], df.Biohazard[i], df.Can_Decontaminate[i],
                  df.Decon_Bin[i])
    WASTE_IMAGE = WASTE.load_image(80 * width / 800)
    BinArray = []
    BinArray.append(Bin(item_path="images/Bin_Autoclave.png", position=(0, 300 * width / 800), bin_type="Autoclave"))
    BinArray.append(
        Bin(item_path="images/Bin Hazardous.png", position=(100 * width / 800, 300 * width / 800), bin_type="Yellow"))
    BinArray.append(
        Bin(item_path="images/Bin_Glass.png", position=(200 * width / 800, 300 * width / 800), bin_type="Glass"))
    BinArray.append(
        Bin(item_path="images/Bin_Sharps.png", position=(300 * width / 800, 300 * width / 800), bin_type="Sharps"))
    BinArray.append(
        Bin(item_path="images/Bin_General.png", position=(400 * width / 800, 300 * width / 800), bin_type="General"))
    BinArray.append(
        Bin(item_path="images/BinRecycling.png", position=(500 * width / 800, 300 * width / 800), bin_type="Recycling"))
    BinArray.append(
        Bin(item_path="images/BinCytotoxic.png", position=(600 * width / 800, 300 * width / 800), bin_type="Cytotoxic"))
    BinArray.append(
        Bin(item_path="images/Bin_Other.png", position=(700 * width / 800, 300 * width / 800), bin_type="Other"))

    images = [(LAB, (0, 0)), (BinArray[0].load_image(75 * width / 800), (0, binheight)),
              (BinArray[1].load_image(75 * width / 800), (100 * width / 800, binheight)),
              (BinArray[2].load_image(75 * width / 800), (200 * width / 800, binheight)),
              (BinArray[3].load_image(75 * width / 800), (300 * width / 800, binheight)),
              (BinArray[4].load_image(75 * width / 800), (400 * width / 800, binheight)),
              (BinArray[5].load_image(75 * width / 800), (500 * width / 800, binheight)),
              (BinArray[6].load_image(75 * width / 800), (600 * width / 800, binheight)),
              (BinArray[7].load_image(75 * width / 800), (700 * width / 800, binheight))]

    scoreboard.reset()
    bonusscoreboard.reset()

    ## set initial image position
    waste_x = random.randrange(0, width)
    waste_y = 0
    move_right = False
    move_left = False
    move_down = False

    x_change = 0
    MAX_x_SPEED = 10
    y_change = 1
    decontaminate = False
    Bacteria = Item("images/LiveBacteria.png").load_image(70 * width / 800)

    while run:
        clock.tick(FPS)  # keep image at FPS 60 on all devices
        draw(WIN, images)  # draw all static images
        WIN.blit(WASTE_IMAGE, (waste_x, waste_y))  # draw image of waste
        font = pygame.font.SysFont("calibri", int(0.04 * width), bold=True, italic=False)
        WIN.blit(font.render(df.Waste[i], True, (0, 0, 0)),
                 (100 * width / 800, 20 * width / 800))  # display waste name on screen
        if WASTE.biohazard:
            WIN.blit(Bacteria, (20 * width / 800, 20 * width / 800))
        scoreboard.display(count, WIN)
        bonusscoreboard.bonusdisplay(WIN)

        pygame.display.update()  # show your drawings on screen

        if count == 21:  # if user presses clicks X
            break

        for event in pygame.event.get():  # loop through all events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:  # if user presses right arrow key
                    move_right = True
                    x_change = 2  # initial speed
                if event.key == pygame.K_LEFT:  # if user presses left arrow key
                    move_left = True
                    x_change = -2  # initial speed
                if event.key == pygame.K_DOWN:  # if user presses left arrow key
                    move_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:  # if user releases right arrow key
                    move_right = False
                    x_change = 0  # stop waste
                if event.key == pygame.K_LEFT:  # if user releases left arrow key
                    move_left = False
                    x_change = 0  # stop waste
                if event.key == pygame.K_DOWN:  # if user presses left arrow key
                    move_down = False
                    y_change = 1  # reset step falling speed
                if event.key == pygame.K_SPACE and not decontaminate and WASTE.decon:
                    decontaminate = True
                    Bacteria = Item("images/DeadBacteria.png").load_image(70 * width / 800)
                    WASTE.set_bintype(WASTE.decon_bin)

            elif event.type == VIDEORESIZE:
                WIN.blit(pygame.transform.scale(LAB, event.dict['size']), (0, 0))
                pygame.display.update()

            elif event.type == pygame.QUIT:  # if user presses clicks X
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

        if waste_y > height:  # if object moves off screen
            correct_bin = WASTE.get_bintype()
            actual_bin = which_bin(waste_x, BinArray)
            if correct_bin == actual_bin:
                scoreboard.add()
                if decontaminate:
                    bonusscoreboard.add()

            waste_x = random.randrange(0, width)  # new object falls from different x position on screen
            waste_y = -25  # bring new object at different position
            count = count + 1
            i = choicearray[count]
            WASTE = Waste("images/" + df.Image[i], df.Waste[i], df.Bin[i], df.Biohazard[i], df.Can_Decontaminate[i],
                          df.Decon_Bin[i])
            WASTE_IMAGE = WASTE.load_image(80 * width / 800)  # select random waste
            Bacteria = Item("images/LiveBacteria.png").load_image(70 * width / 800)
            decontaminate = False


def which_bin(waste_x, binarray):
    width = WIN.get_width()
    for bin in binarray:
        bin_position = bin.get_position()
        x_position = bin_position[0] - 40 * width / 800
        if x_position <= waste_x < (x_position + 100 * width / 800):
            return bin.get_bintype()
    return "Null"


def main_menu(screen, clock, FPS):

    pygame.display.set_caption("Main Menu")
    run = True
    bright_green = (0, 255, 0)
    bright_red = (255, 0, 0)
    red = (200, 0, 0)
    green = (0, 200, 0)
    screen.fill((0, 0, 0))
    WIDTH = WIN.get_width()
    HEIGHT = WIN.get_height()
    LAB = Item("images/labBlur.jpg").load_image(WIDTH)
    MONSTER = Item("images/Mattie_Monster.png").load_image(WIDTH*0.5)
    WIN.blit(LAB, (0, 0))
    WIN.blit(MONSTER, (WIDTH*0.25, HEIGHT*0.75))



    # pygame.mixer.music.load('background_music_wav.wav')
    # pygame.mixer.music.play(-1)
    while run:



        WIDTH = WIN.get_width()
        HEIGHT = WIN.get_height()
        font_large = pygame.font.SysFont("calibri", int(0.04 * WIDTH), bold=True, italic=False)
        font = pygame.font.SysFont("calibri", int(0.025 * WIDTH), bold=True, italic=False)
        instructfont = pygame.font.SysFont("calibri", int(0.025 * WIDTH), bold=False, italic=False)

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                run = False

            elif event.type == VIDEORESIZE:
                WIDTH, HEIGHT = event.size
                HEIGHT = WIDTH * 525 / 800
                screen = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)
                pygame.display.update()

            width = WIDTH * 100 / 800
            height = HEIGHT * 50 / 525

            xposition = WIDTH * 600 / 800
            ypostiongreen = HEIGHT * 350 / 525
            ypostionred = HEIGHT * 400 / 525

            LAB = Item("images/labBlur.jpg").load_image(WIDTH)
            MONSTER = Item("images/Mattie_Monster.png").load_image(WIDTH*0.5)
            WIN.blit(LAB, (0, 0))
            WIN.blit(MONSTER, (WIDTH * 0.25, HEIGHT * 0.4))

            if xposition + width > mouse[0] > xposition and ypostiongreen + height > mouse[1] > ypostiongreen:
                pygame.draw.rect(screen, bright_green, (xposition, ypostiongreen, width, height))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    main()
            else:
                pygame.draw.rect(screen, green, (xposition, ypostiongreen, width, height))

            if xposition + width > mouse[0] > xposition and ypostionred + 75 * HEIGHT / 525 > mouse[1] > ypostionred:
                pygame.draw.rect(screen, bright_red, (xposition, ypostionred, width, height))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
                    break
            else:
                pygame.draw.rect(screen, red, (xposition, ypostionred, width, height))

            # screen.blit(font_large.render("Waste Disposal Game", True, (255, 255, 255)), (325, 50))

            screen.blit(font.render("Play", True, (0, 0, 0)), ((xposition + 25), (ypostiongreen + 18 * HEIGHT / 525)))
            screen.blit(font.render("Quit", True, (0, 0, 0)), ((xposition + 25), (ypostionred + 18 * HEIGHT / 525)))
            screen.blit(font_large.render("Waste Disposal Game!", True, (0, 0, 0)),
                        (260 * WIDTH / 800, 25 * HEIGHT / 525))
            screen.blit(
                instructfont.render("Press arrow keys to move the waste in to the correct bin", True, (0, 0, 0)),
                (20 * WIDTH / 800, 90 * HEIGHT / 525))
            screen.blit(
                instructfont.render("If you see the bacteria sign in the top right your waste is contaminated with a GMO.",
                                    True, (0, 0, 0)), (20 * WIDTH / 800, 120 * HEIGHT / 525))
            screen.blit(
                instructfont.render("Press the space bar to decontaminate your waste where possible for extra points.",
                True, (0, 0, 0)), (20 * WIDTH / 800, 140 * HEIGHT / 525))
            screen.blit(
                font_large.render("Final Score: " + str(scoreboard.number + bonusscoreboard.number) + " / 20", True,
                                  (0, 0, 0)),
                (300 * WIDTH / 800, 180 * HEIGHT / 525))
            # screen.blit(font_large.render("Bonus Points: " + str(bonusscoreboard.number), True, (0, 0, 0)), (300, 250))

        pygame.display.flip()
        clock.tick(FPS)


pygame.quit()

global WIN

# initialize mixer
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

WIN = pygame.display.set_mode((800, 525), pygame.RESIZABLE)

scoreboard = Score(0, 650, 10)
bonusscoreboard = Score(0, 650, 30)
#LAB = pygame.image.load("images/lab.jpg")
#WIDTH, HEIGHT = LAB.get_width(), LAB.get_height()
#WIN.blit(LAB, (WIDTH, HEIGHT))

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

main_menu(WIN, clock, FPS)
