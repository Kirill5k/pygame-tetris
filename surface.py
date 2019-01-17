import pygame
from content.color import Color
from config import *


class Surface:
    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.__draw_window()
        self.__init_field()
        self.__draw_field()
        self.__update_display()

    def __draw_window(self):
        self.window.fill(Color.BLACK.value)
        pygame.font.init()
        font = pygame.font.SysFont(FONT_FAMILY, FONT_SIZE)
        label = font.render(TITLE, 1, Color.WHITE.value)
        self.window.blit(label, (TOP_LEFT_X + FIELD_WIDTH / 2 - label.get_width() / 2, BLOCK_SIZE))

    def __init_field(self):
        self.height = FIELD_HEIGHT / BLOCK_SIZE
        self.width = FIELD_WIDTH / BLOCK_SIZE
        self.field = [Color.BLACK.value for _ in range(self.width) for _ in range(self.height)]

    def __draw_field(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                x = TOP_LEFT_X + j * BLOCK_SIZE
                y = TOP_LEFT_Y + i * BLOCK_SIZE
                pygame.draw.rect(self.window, self.field[i][j], (x, y, BLOCK_SIZE, BLOCK_SIZE), 0)

        pygame.draw.react(self.window, Color.RED.value, (TOP_LEFT_X, TOP_LEFT_Y, self.width, self.height), BORDER_SIZE)

    def __draw_grid(self):
        for i in range(len(self.field)):
            pygame.draw.line(self.window)
            for j in range(len(self.field[i])):


    @staticmethod
    def __update_display():
        pygame.display.update()

    def update(self):
        self.__draw_field()
        self.__update_display()

    def update_field(self, locked_positions):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if locked_positions is not None and (j, i) in locked_positions:
                    self.field[i][j] = locked_positions[(j, i)]
