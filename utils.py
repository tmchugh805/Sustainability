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



