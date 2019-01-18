import pygame
from content.color import Color
from content.piece import Piece
from utils.iterators import field_cell_iterator
from config import *


class Surface:
    def __init__(self, window):
        self.window = window
        self.height = int(FIELD_HEIGHT / BLOCK_SIZE)
        self.width = int(FIELD_WIDTH / BLOCK_SIZE)
        self.all_positions = [(j, i) for j in range(self.width) for i in range(self.height)]
        self.locked_positions = {}
        self.__draw_window()
        self.__init_field()
        self.__draw_field()
        self.__draw_grid()
        self.__update_display()

    def __draw_window(self):
        self.window.fill(Color.BLACK.value)
        pygame.font.init()
        font = pygame.font.SysFont(FONT_FAMILY, FONT_SIZE)
        label = font.render(TITLE, 1, Color.WHITE.value)
        self.window.blit(label, (TOP_LEFT_X + FIELD_WIDTH / 2 - label.get_width() / 2, BLOCK_SIZE))

    def __init_field(self):
        self.field = [[Color.BLACK.value for _ in range(self.width)] for _ in range(self.height)]

    def __draw_field(self):
        for row_num, cell_num in field_cell_iterator(self.field):
            x = TOP_LEFT_X + cell_num * BLOCK_SIZE
            y = TOP_LEFT_Y + row_num * BLOCK_SIZE
            pygame.draw.rect(self.window, self.field[row_num][cell_num], (x, y, BLOCK_SIZE, BLOCK_SIZE), 0)

        pygame.draw.rect(self.window, Color.RED.value, (TOP_LEFT_X, TOP_LEFT_Y, FIELD_WIDTH, FIELD_HEIGHT), BORDER_SIZE)

    def __draw_grid(self):
        for i in range(len(self.field)):
            hor_line_start = (TOP_LEFT_X, TOP_LEFT_Y + i * BLOCK_SIZE)
            hor_line_end = (TOP_LEFT_X + FIELD_WIDTH, TOP_LEFT_Y + i * BLOCK_SIZE)
            pygame.draw.line(self.window, Color.GREY.value, hor_line_start, hor_line_end)

        for j in range(len(self.field[0])):
            vert_line_start = (TOP_LEFT_X + j * BLOCK_SIZE, TOP_LEFT_Y)
            vert_line_end = (TOP_LEFT_X + j * BLOCK_SIZE, TOP_LEFT_Y + FIELD_HEIGHT)
            pygame.draw.line(self.window, Color.GREY.value, vert_line_start, vert_line_end)

    @staticmethod
    def __update_display():
        pygame.display.update()

    def update(self):
        self.__draw_field()
        self.__draw_grid()
        self.__update_display()

    def is_valid_position(self, piece: Piece):
        accepted_positions = [pos for pos in self.all_positions if self.field[pos[1]][pos[0]] == Color.BLACK.value]
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

    def update_locked_positions(self):
        self.__init_field()
        for row_num, cell_num in field_cell_iterator(self.field):
            if (cell_num, row_num) in self.locked_positions:
                self.field[row_num][cell_num] = self.locked_positions[(cell_num, row_num)]

    @property
    def is_game_over(self):
        for (x, y) in self.locked_positions:
            if y < 1:
                return True
        return False
