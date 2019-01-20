import pygame
from content import Text, Color
from elements import Piece, NextPieceField, Grid
from config import *


def create_label(text, size=FONT_SIZE, color=Color.WHITE, font=FONT_FAMILY):
    font = pygame.font.SysFont(font, int(size))
    return font.render(text, 1, color)


class Surface:
    def __init__(self, window):
        self.window = window

        grid_top_x = (SCREEN_WIDTH - FIELD_WIDTH) // 2
        grid_top_y = SCREEN_HEIGHT - FIELD_HEIGHT

        self.add_fields_x = grid_top_x + FIELD_WIDTH + BLOCK_SIZE * 2
        self.next_piece_y = grid_top_y + int(FIELD_HEIGHT / 4)

        self.__draw_static_text()
        self.grid = Grid(window, grid_top_x, grid_top_y, FIELD_WIDTH, FIELD_HEIGHT, BLOCK_SIZE, BORDER_SIZE)
        self.next_piece_field = NextPieceField(window, self.add_fields_x, self.next_piece_y, BLOCK_SIZE)
        self.update()

    def __draw_static_text(self):
        header_label = create_label(Text.TITLE)
        self.window.blit(header_label, (SCREEN_WIDTH / 2 - header_label.get_width() / 2, BLOCK_SIZE))

        next_shape_label = create_label(Text.NEXT_SHAPE, size=FONT_SIZE / 2)
        self.window.blit(next_shape_label, (self.add_fields_x + BLOCK_SIZE / 3, self.next_piece_y - BLOCK_SIZE))

    def update(self):
        self.grid.update()
        pygame.display.update()

    def is_valid_pos(self, piece: Piece):
        return self.grid.is_valid_pos(piece)

    def add_piece(self, piece: Piece):
        self.grid.add_piece(piece)

    def lock_piece(self, piece: Piece):
        self.grid.lock_piece(piece)

    def clear_moving_pieces(self):
        self.grid.clear_moving_pieces()

    def clear_rows(self):
        return self.grid.clear_rows()

    def draw_next_piece(self, piece: Piece):
        self.next_piece_field.update(piece)

    def update_score(self, new_score):
        pass

    @property
    def is_overfilled(self):
        return self.grid.is_overfilled
