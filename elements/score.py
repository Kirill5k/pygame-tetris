import pygame
from content import Color


class ScoreField:
    MAX_SCORE_LENGTH = 6
    SCORE_FIELD_OFFSET = 1.2

    def __init__(self, window, top_x, top_y, font_family, font_size):
        self.window = window
        self.top_x = top_x
        self.top_y = top_y
        self.zone_rect = pygame.Rect(top_x, top_y, font_size * self.MAX_SCORE_LENGTH * self.SCORE_FIELD_OFFSET, font_size * self.SCORE_FIELD_OFFSET)
        self.font = pygame.font.SysFont(font_family, font_size)
        self.update(0)

    def update(self, score):
        self.window.fill(Color.BLACK, self.zone_rect)

        score_str = str(score)
        score_display_str = ('0' * (self.MAX_SCORE_LENGTH - len(score_str))) + score_str
        label = self.font.render(score_display_str, 1, Color.YELLOW)
        self.window.blit(label, (self.top_x, self.top_y))
