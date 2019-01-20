import pygame
from content import Text, Color
from elements import Piece
from elements.next import NextPieceField
from utils.grid import create_empty_rows, grid_iterator
from config import *


def create_label(text, size=FONT_SIZE, color=Color.WHITE, font=FONT_FAMILY):
    font = pygame.font.SysFont(font, int(size))
    return font.render(text, 1, color)


class Surface:
    rows_count = int(FIELD_HEIGHT / BLOCK_SIZE)
    columns_count = int(FIELD_WIDTH / BLOCK_SIZE)
    add_fields_x = TOP_LEFT_X + FIELD_WIDTH + BLOCK_SIZE * 2
    next_piece_y = TOP_LEFT_Y + int(FIELD_HEIGHT / 4)

    def __init__(self, window):
        self.window = window
        self.all_positions = [(col, row) for row, col in grid_iterator(self.rows_count, self.columns_count)]
        self.field = create_empty_rows(self.columns_count, self.rows_count)
        self.locked_positions = {}
        self.__draw_static_elements()
        self.next_piece_field = NextPieceField(window, self.add_fields_x, self.next_piece_y, BLOCK_SIZE)
        self.update()

    def __draw_static_elements(self):
        header_label = create_label(Text.TITLE)
        self.window.blit(header_label, (TOP_LEFT_X + FIELD_WIDTH / 2 - header_label.get_width() / 2, BLOCK_SIZE))

        next_shape_label = create_label(Text.NEXT_SHAPE, size=FONT_SIZE / 2)
        self.window.blit(next_shape_label, (self.add_fields_x + BLOCK_SIZE / 3, self.next_piece_y - BLOCK_SIZE))

    def __draw_field(self):
        for row_num, cell_num in grid_iterator(self.rows_count, self.columns_count):
            x = TOP_LEFT_X + cell_num * BLOCK_SIZE
            y = TOP_LEFT_Y + row_num * BLOCK_SIZE
            pygame.draw.rect(self.window, self.field[row_num][cell_num], (x, y, BLOCK_SIZE, BLOCK_SIZE), 0)

        pygame.draw.rect(self.window, Color.RED, (TOP_LEFT_X, TOP_LEFT_Y, FIELD_WIDTH, FIELD_HEIGHT), BORDER_SIZE)

    def __draw_grid(self):
        for row_num in range(self.rows_count):
            hor_line_start = (TOP_LEFT_X, TOP_LEFT_Y + row_num * BLOCK_SIZE)
            hor_line_end = (TOP_LEFT_X + FIELD_WIDTH, TOP_LEFT_Y + row_num * BLOCK_SIZE)
            pygame.draw.line(self.window, Color.GREY, hor_line_start, hor_line_end)

        for cell_num in range(self.columns_count):
            vert_line_start = (TOP_LEFT_X + cell_num * BLOCK_SIZE, TOP_LEFT_Y)
            vert_line_end = (TOP_LEFT_X + cell_num * BLOCK_SIZE, TOP_LEFT_Y + FIELD_HEIGHT)
            pygame.draw.line(self.window, Color.GREY, vert_line_start, vert_line_end)

    def update(self):
        self.__draw_field()
        self.__draw_grid()
        pygame.display.update()

    def is_valid_pos(self, piece: Piece):
        accepted_positions = [pos for pos in self.all_positions if self.field[pos[1]][pos[0]] is Color.BLACK]
        for pos in piece.shape_positions:
            if pos not in accepted_positions and pos[1] > -1:
                return False
        return True

    def add_piece(self, piece: Piece):
        for pos_x, pos_y in piece.shape_positions:
            if pos_y > -1:
                self.field[pos_y][pos_x] = piece.shape.color

    def lock_piece(self, piece: Piece):
        for pos in piece.shape_positions:
            self.locked_positions[pos] = piece.shape.color

    def clear_moving_pieces(self):
        self.field = create_empty_rows(self.columns_count, self.rows_count)
        for row_num, cell_num in grid_iterator(self.rows_count, self.columns_count):
            if (cell_num, row_num) in self.locked_positions:
                self.field[row_num][cell_num] = self.locked_positions[(cell_num, row_num)]

    def clear_rows(self):
        new_field = list(filter(lambda row: Color.BLACK in row, self.field))
        if len(new_field) is not len(self.field):
            deleted_rows_count = len(self.field) - len(new_field)
            self.field = create_empty_rows(self.columns_count, deleted_rows_count) + new_field
            self.locked_positions = {}
            for row_num, cell_num in grid_iterator(self.rows_count, self.columns_count):
                if self.field[row_num][cell_num] is not Color.BLACK:
                    self.locked_positions[(cell_num, row_num)] = self.field[row_num][cell_num]
            return deleted_rows_count
        return 0

    def draw_next_piece(self, piece: Piece):
        self.next_piece_field.update(piece)

    def update_score(self, new_score):
        pass

    @property
    def is_overfilled(self):
        for (x, y) in self.locked_positions:
            if y < 1:
                return True
        return False
