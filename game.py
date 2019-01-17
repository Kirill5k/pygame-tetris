import pygame
from content.piece import Piece
from content.color import Color
from setup import create_surface


def convert_shape_format(shape):
    pass


def valid_space(shape, grid):
    pass


def check_lost(positions):
    pass


def draw_text_middle(text, size, color, surface):
    pass


def clear_rows(grid, locked):
    pass


def draw_next_shape(shape, surface):
    pass


def main(surface):
    current_piece = Piece.get_random(5, 0)
    next_piece = Piece.get_random(5, 0)
    clock = pygame.time.Clock()
    fall_time = 0
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.move_left()
                if event.key == pygame.K_RIGHT:
                    current_piece.move_right()
                if event.key == pygame.K_DOWN:
                    current_piece.move_down()
                if event.key == pygame.K_UP:
                    current_piece.rotate()

        surface.update()


def main_menu(surface):
    main(surface)


surface = create_surface()
main_menu(surface)  # start game
