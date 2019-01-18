import pygame
from surface import Surface
from config import *


pygame.font.init()
pygame.display.set_caption(TITLE)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def create_surface():
    return Surface(window)


def quit_game():
    pygame.display.quit()


