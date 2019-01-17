import pygame
from surface import Surface
from config import *


pygame.font.init()
pygame.display.set_caption(TITLE)


def create_surface():
    return Surface()
