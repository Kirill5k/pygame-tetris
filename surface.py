import pygame
from content import Text, Color, Piece
from utils.grid import create_empty_row, grid_iterator
from config import *


def create_label(text, size=FONT_SIZE, color=Color.WHITE):
    font = pygame.font.SysFont(FONT_FAMILY, int(size))
    return font.render(text, 1, color)


class Surface:
    def __init__(self, window):
        self.window = window
        self.rows_count = int(FIELD_HEIGHT / BLOCK_SIZE)
        self.columns_count = int(FIELD_WIDTH / BLOCK_SIZE)
        self.all_positions = [(col, row) for row, col in grid_iterator(self.rows_count, self.columns_count)]
        self.locked_positions = {}
        self.__init_field()
        self.__init_next_shape()
        self.__draw_window()
        self.__draw_field()
        self.__draw_grid()
        self.__update_display()

    def __draw_window(self):
        self.window.fill(Color.BLACK)
        label = create_label(Text.TITLE)
        self.window.blit(label, (TOP_LEFT_X + FIELD_WIDTH / 2 - label.get_width() / 2, BLOCK_SIZE))

    def __init_field(self):
        self.field = [create_empty_row(self.columns_count) for _ in range(self.rows_count)]

    def __init_next_shape(self):
        self.next_shape_x = TOP_LEFT_X + FIELD_WIDTH + BLOCK_SIZE * 2
        self.next_shape_y = TOP_LEFT_Y + int(FIELD_HEIGHT / 4)
        self.next_shape_rect = pygame.Rect(self.next_shape_x, self.next_shape_y, BLOCK_SIZE * 5, BLOCK_SIZE * 4)

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

    @staticmethod
    def __update_display():
        pygame.display.update()

    def update(self):
        self.__draw_field()
        self.__draw_grid()
        self.__update_display()

    def is_valid_pos(self, piece: Piece):
        accepted_positions = [pos for pos in self.all_positions if self.field[pos[1]][pos[0]] == Color.BLACK]
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
        self.__init_field()
        for row_num, cell_num in grid_iterator(self.rows_count, self.columns_count):
            if (cell_num, row_num) in self.locked_positions:
                self.field[row_num][cell_num] = self.locked_positions[(cell_num, row_num)]

    def clear_rows(self):
        new_field = list(filter(lambda row: Color.BLACK in row, self.field))
        if len(new_field) != len(self.field):
            deleted_rows_count = len(self.field) - len(new_field)
            self.field = [create_empty_row(self.columns_count)] * deleted_rows_count + new_field
            self.locked_positions = {}
            for row_num, cell_num in grid_iterator(self.rows_count, self.columns_count):
                if self.field[row_num][cell_num] != Color.BLACK:
                    self.locked_positions[(cell_num, row_num)] = self.field[row_num][cell_num]

    def draw_next(self, piece: Piece):
        label = create_label(Text.NEXT_SHAPE, size=FONT_SIZE / 2)
        self.window.blit(label, (self.next_shape_x + BLOCK_SIZE / 3, self.next_shape_y - BLOCK_SIZE * 1.5))
        self.window.fill(Color.BLACK, self.next_shape_rect)
        for cell_num, row_num in piece.shape_iterator():
            x = self.next_shape_x + cell_num * BLOCK_SIZE
            y = self.next_shape_y + row_num * BLOCK_SIZE
            pygame.draw.rect(self.window, piece.shape.color, (x, y, BLOCK_SIZE, BLOCK_SIZE), 0)

    @property
    def is_overfilled(self):
        for (x, y) in self.locked_positions:
            if y < 1:
                return True
        return False
