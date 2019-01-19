import pygame
from elements import Surface, Game
from content import Text, Color
from config import *


pygame.font.init()
pygame.display.set_caption(Text.TITLE)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window.fill(Color.BLACK)

game = Game()
surface = Surface(window)
