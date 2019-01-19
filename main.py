import pygame
from setup import game, surface

actions_keys = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]

action_keys_actions_map = {
    pygame.K_LEFT: lambda piece: piece.move_left(),
    pygame.K_RIGHT: lambda piece: piece.move_right(),
    pygame.K_DOWN: lambda piece: piece.move_down(),
    pygame.K_UP: lambda piece: piece.rotate()
}


def draw_text_middle(text, size, color, surface):
    pass


if __name__ == '__main__':
    change_piece = False
    surface.draw_next_piece(game.next_piece)

    while game.is_running:
        game.clock_tick()

        if game.cycle_has_passed:
            game.reset_time()
            game.current_piece.move_down()
            if not surface.is_valid_pos(game.current_piece) and game.current_piece.is_in_the_field:
                game.current_piece.undo_action()
                change_piece = True
            else:
                game.current_piece.perform_action()

        for event in game.key_events():
            if event.key == pygame.K_ESCAPE:
                game.quit()
            if event.key in actions_keys:
                action_keys_actions_map[event.key](game.current_piece)
                if surface.is_valid_pos(game.current_piece):
                    game.current_piece.perform_action()
                else:
                    game.current_piece.undo_action()

        surface.add_piece(game.current_piece)
        surface.update()

        if change_piece:
            surface.lock_piece(game.current_piece)
            game.change_piece()
            change_piece = False
            surface.draw_next_piece(game.next_piece)
            cleared_rows_count = surface.clear_rows()
            if cleared_rows_count > 0:
                game.add_score(cleared_rows_count)
                surface.update_score(game.score)

        surface.clear_moving_pieces()

        if surface.is_overfilled:
            game.stop()

