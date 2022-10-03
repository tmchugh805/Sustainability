import pygame
from score import score


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
    def __init__(self, item_path: str=None, waste_type: str=None):
        super().__init__(item_path)
        self.waste_type = waste_type
if __name__ == "__main__":
    print(scale_image(Item("images/Bin.png").load_image(), 75))

# create an item class
# create a bin class that inherits from am item class 
# bin class should have positon and type attribute
# create waste class
# waste class should have type attribute 


