import pygame


class score:

    number = 0
    x_position = 0
    y_position = 0


    def __init__(self, number, x_position, y_position):
        self.number = number
        self.x_position = x_position
        self.y_position = y_position

    def add(self):
        self.number = self.number + 1

    def subtract(self):
        self.number = self.number - 1

    def setposition(self, x, y):
        self.x_position = x
        self.y_position = y

    def display(self, screen):
        myfont = pygame.font.SysFont("calibri", 24, bold=True, italic=False)
        RED = (255, 0, 0)
        label = myfont.render("Score: "+str(self.number), 1, RED)
        screen.blit(label, (self.x_position, self.y_position))
        pygame.display.update()

    def reset(self):
        self.number = 0
