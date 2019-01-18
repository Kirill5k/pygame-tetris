import pygame
from setup import game, surface


def draw_text_middle(text, size, color, surface):
    pass


def clear_rows(grid, locked):
    pass


def draw_next_shape(shape, surface):
    pass


if __name__ == '__main__':
    change_piece = False

    while game.is_running:
        game.clock_tick()

        if game.cycle_has_passed:
            game.reset_time()
            game.current_piece.move_down()
            if not surface.is_valid_pos(game.current_piece) and game.current_piece.is_moving:
                game.current_piece.move_up()
                change_piece = True

        for event in game.key_events():
            if event.key == pygame.K_ESCAPE:
                game.quit()
            if event.key == pygame.K_LEFT:
                game.current_piece.move_left()
                if not surface.is_valid_pos(game.current_piece):
                    game.current_piece.move_right()
            if event.key == pygame.K_RIGHT:
                game.current_piece.move_right()
                if not surface.is_valid_pos(game.current_piece):
                    game.current_piece.move_left()
            if event.key == pygame.K_DOWN:
                game.current_piece.move_down()
                if not surface.is_valid_pos(game.current_piece):
                    game.current_piece.move_up()
            if event.key == pygame.K_UP:
                game.current_piece.rotate()
                if not surface.is_valid_pos(game.current_piece):
                    game.current_piece.rotate_back()

        surface.add_piece(game.current_piece)
        surface.update()

        if change_piece:
            surface.lock_piece(game.current_piece)
            game.change_piece()
            change_piece = False

        surface.clear_moving_pieces()

        if surface.is_overfilled:
            game.stop()

