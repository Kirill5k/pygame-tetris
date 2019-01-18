import pygame
from surface import Surface
from game import Game
from content.text import Text
from config import *


pygame.font.init()
pygame.display.set_caption(Text.TITLE)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game = Game()
surface = Surface(window)
