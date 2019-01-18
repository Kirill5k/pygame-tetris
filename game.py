import pygame
from content.piece import Piece


class Game:
    MS_IN_SECONDS = 1000

    def __init__(self, starting_speed=0.27):
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.fall_time = 0
        self.fall_speed = starting_speed
        self.current_piece: Piece = Piece.get_random()
        self.next_piece: Piece = Piece.get_random()

    def clock_tick(self):
        self.fall_time += self.clock.get_rawtime()
        self.clock.tick()

    def key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                yield event

    def change_piece(self):
        self.current_piece = self.next_piece
        self.next_piece = Piece.get_random()

    def reset_time(self):
        self.fall_time = 0

    def stop(self):
        self.is_running = False

    @property
    def cycle_has_passed(self):
        return self.fall_time / self.MS_IN_SECONDS > self.fall_speed

    @staticmethod
    def quit():
        pygame.display.quit()

