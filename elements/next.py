import pygame
from content import Color
from elements import Piece


class NextPieceField:
    def __init__(self, window, top_x, top_y, block_size):
        self.window = window
        self.top_x = top_x
        self.top_y = top_y
        self.block_size = block_size
        self.zone_rect = pygame.Rect(top_x, top_y, block_size * 5, block_size * 5)

    def update(self, piece: Piece):
        self.window.fill(Color.BLACK, self.zone_rect)
        for cell_num, row_num in piece.shape_iterator():
            x = self.top_x + cell_num * self.block_size
            y = self.top_y + row_num * self.block_size
            pygame.draw.rect(self.window, piece.shape.color, (x, y, self.block_size, self.block_size), 0)
