import pygame
from score import score


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def draw(win, images):
    """A function to draw images"""
    for img, pos in images:
        win.blit(img, pos)



