from random import choice
from content.shape import Shape


class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.rotation = 0

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1

    def rotate(self):
        self.rotation += 1

    @classmethod
    def get_random(cls, x, y):
        return Piece(x, y, choice(list(Shape)))
