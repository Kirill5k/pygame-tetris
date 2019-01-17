import pygame
from content.piece import Piece
from content.color import Color
from setup import create_surface


def convert_shape_format(piece):
    positions = []
    format = piece.shape[piece.rotation % len(piece.shape)]


def draw_text_middle(text, size, color, surface):
    pass


def clear_rows(grid, locked):
    pass


def draw_next_shape(shape, surface):
    pass


def main(surface):
    locked_positions = {}
    current_piece = Piece.get_random(5, 0)
    next_piece = Piece.get_random(5, 0)
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    run = True
    change_piece = False

    while run:
        surface.update_locked_positions()
        fall_time += clock.get_rawtime()
        clock.tick()


        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.move_down()
            if not surface.is_valid_position(current_piece) and current_piece.is_moving:
                current_piece.move_up()
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.move_left()
                    if not surface.is_valid_position(current_piece):
                        current_piece.move_right()
                if event.key == pygame.K_RIGHT:
                    current_piece.move_right()
                    if not surface.is_valid_position(current_piece):
                        current_piece.move_left()
                if event.key == pygame.K_DOWN:
                    current_piece.move_down()
                    if not surface.is_valid_position(current_piece):
                        current_piece.move_up()
                if event.key == pygame.K_UP:
                    current_piece.rotate()
                    if not surface.is_valid_position(current_piece):
                        current_piece.rotate_back()

        surface.add_piece(current_piece)

        if change_piece:
            surface.lock_piece(current_piece)
            current_piece = next_piece
            next_piece = Piece.get_random()
            change_piece = False

        surface.update()

        if surface.is_game_over:
            run = False

    pygame.display.quit()


def main_menu(surface):
    main(surface)


surface = create_surface()
main_menu(surface)  # start game
