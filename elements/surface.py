import pygame
from content import Text, Color
from elements import Piece, ScoreField, NextPieceField, Grid
from config import *


class Surface:
    grid_top_x = (SCREEN_WIDTH - FIELD_WIDTH) // 2
    grid_top_y = SCREEN_HEIGHT - FIELD_HEIGHT
    add_fields_x = grid_top_x + FIELD_WIDTH + BLOCK_SIZE * 2
    next_piece_y = grid_top_y + FIELD_HEIGHT // 4
    score_field_y = grid_top_y + BLOCK_SIZE

    def __init__(self, window):
        self.window = window

        self.__draw_static_text()
        self.grid = Grid(window, self.grid_top_x, self.grid_top_y, FIELD_WIDTH, FIELD_HEIGHT, BLOCK_SIZE, BORDER_SIZE)
        self.next_piece_field = NextPieceField(window, self.add_fields_x, self.next_piece_y, BLOCK_SIZE)
        self.score_field = ScoreField(window, self.add_fields_x, self.score_field_y, SECONDARY_FONT_FAMILY, SECONDARY_FONT_SIZE)

    def __draw_label(self, text, x, y, font_family=FONT_FAMILY, font_size=SECONDARY_FONT_SIZE, color=Color.WHITE, bold=False):
        font = pygame.font.SysFont(font_family, font_size, bold=bold)
        label = font.render(text, 1, color)
        self.window.blit(label, (x, y))

    def __draw_static_text(self):
        self.__draw_label(Text.TITLE, x=SCREEN_WIDTH//2 - BLOCK_SIZE * 2, y=BLOCK_SIZE, font_size=PRIMARY_FONT_SIZE)
        self.__draw_label(Text.NEXT_SHAPE, x=self.add_fields_x, y=self.next_piece_y-BLOCK_SIZE)
        self.__draw_label(Text.SCORE, x=self.add_fields_x, y=self.score_field_y-BLOCK_SIZE)

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
        self.score_field.update(new_score)

    @property
    def is_overfilled(self):
        is_overfilled = self.grid.is_overfilled
        if is_overfilled:
            self.__draw_label(Text.GAME_OVER, BLOCK_SIZE * 7, SCREEN_HEIGHT // 2 - BLOCK_SIZE,
                              font_family=SECONDARY_FONT_FAMILY,
                              bold=True,
                              font_size=PRIMARY_FONT_SIZE,
                              color=Color.YELLOW)
            pygame.display.update()
        return is_overfilled
