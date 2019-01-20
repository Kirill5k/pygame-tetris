import pygame
from elements.piece import Piece
from content.color import Color
from utils.grid import create_empty_rows, grid_iterator


class Grid:
    def __init__(self, window, top_x, top_y, width, height, block_size, border_size):
        self.window = window
        self.top_x = top_x
        self.top_y = top_y
        self.width = width
        self.height = height
        self.block_size = block_size
        self.border_size = border_size
        self.rows_count = int(height / block_size)
        self.columns_count = int(width / block_size)
        self.field = create_empty_rows(self.columns_count, self.rows_count)
        self.locked_positions = {}
        self.all_positions = [(col, row) for row, col in grid_iterator(self.columns_count, self.rows_count)]

    def __draw_field(self):
        for row_num, cell_num in grid_iterator(self.columns_count, self.rows_count):
            x = self.top_x + cell_num * self.block_size
            y = self.top_y + row_num * self.block_size
            pygame.draw.rect(self.window, self.field[row_num][cell_num], (x, y, self.block_size, self.block_size), 0)

    def __draw_borders(self):
        for row_num in range(self.rows_count):
            hor_line_start = (self.top_x, self.top_y + row_num * self.block_size)
            hor_line_end = (self.top_x + self.width, self.top_y + row_num * self.block_size)
            pygame.draw.line(self.window, Color.GREY, hor_line_start, hor_line_end)

        for cell_num in range(self.columns_count):
            vert_line_start = (self.top_x + cell_num * self.block_size, self.top_y)
            vert_line_end = (self.top_x + cell_num * self.block_size, self.top_y + self.height)
            pygame.draw.line(self.window, Color.GREY, vert_line_start, vert_line_end)

        pygame.draw.rect(self.window, Color.RED, (self.top_x, self.top_y, self.width, self.height), self.border_size)

    def update(self):
        self.__draw_field()
        self.__draw_borders()

    def add_piece(self, piece: Piece):
        for pos_x, pos_y in piece.shape_positions:
            if pos_y > -1:
                self.field[pos_y][pos_x] = piece.shape.color

    def lock_piece(self, piece: Piece):
        for pos in piece.shape_positions:
            self.locked_positions[pos] = piece.shape.color

    def clear_moving_pieces(self):
        self.field = create_empty_rows(self.columns_count, self.rows_count)
        for row_num, cell_num in grid_iterator(self.columns_count, self.rows_count):
            if (cell_num, row_num) in self.locked_positions:
                self.field[row_num][cell_num] = self.locked_positions[(cell_num, row_num)]

    def clear_rows(self):
        new_field = list(filter(lambda row: Color.BLACK in row, self.field))
        if len(new_field) is not len(self.field):
            deleted_rows_count = len(self.field) - len(new_field)
            self.field = create_empty_rows(self.columns_count, deleted_rows_count) + new_field
            self.locked_positions = {}
            for row_num, cell_num in grid_iterator(self.columns_count, self.rows_count):
                if self.field[row_num][cell_num] is not Color.BLACK:
                    self.locked_positions[(cell_num, row_num)] = self.field[row_num][cell_num]
            return deleted_rows_count
        return 0

    @property
    def is_overfilled(self):
        for (x, y) in self.locked_positions:
            if y < 1:
                return True
        return False

    def is_valid_pos(self, piece: Piece):
        accepted_positions = [pos for pos in self.all_positions if self.field[pos[1]][pos[0]] is Color.BLACK]
        for pos in piece.shape_positions:
            if pos not in accepted_positions and pos[1] > -1:
                return False
        return True
