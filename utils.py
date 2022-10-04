import pygame


def scale_image(img, width):
    factor = width / img.get_width()
    size = round(width), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def draw(win, images):
    """A function to draw images"""
    for img, pos in images:
        win.blit(img, pos)


class Item:
    def __init__(self, item_path: str=None):
        self.item_path = item_path

    def load_image(self, factor=False):
        if factor:
            return scale_image(pygame.image.load(self.item_path), factor)
        else:
            return pygame.image.load(self.item_path)


class Bin(Item):
    def __init__(self, item_path: str=None, position: tuple=None, bin_type: str=None):
        super().__init__(item_path)
        self.position = position
        self.bin_type = bin_type


class Waste(Item):
    def __init__(self, item_path: str=None, waste_type: str=None, bin: str=None, bioharzard: bool=False, sharp: bool=False, toxic: bool=False):
        super().__init__(item_path)
        self.waste_type = waste_type
        self.bin = bin
        self.bioharzard = bioharzard
        self.sharp = sharp
        self.toxic = toxic

# create an item class
# create a bin class that inherits from am item class
# bin class should have positon and type attribute
# create waste class
# waste class should have type attribute

class Score:
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
        label = myfont.render("Score: " + str(self.number), 1, RED)
        screen.blit(label, (self.x_position, self.y_position))
        pygame.display.update()

    def reset(self):
        self.number = 0
