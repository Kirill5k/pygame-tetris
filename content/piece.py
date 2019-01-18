from random import choice
from content.shape import Shape


class Piece:
    POS_OFFSET_X = 0 # 2
    POS_OFFSET_Y = 0 # 4

    def __init__(self, x, y, shape: Shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.rotation = 0

    @classmethod
    def get_random(cls, x=5, y=0):
        return Piece(x, y, choice(list(Shape)))

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1

    def move_up(self):
        self.y -= 1

    def rotate(self):
        self.rotation += 1

    def rotate_back(self):
        self.rotation += 1

    @property
    def is_moving(self):
        return self.y > 0

    @property
    def current_form_of_shape(self):
        return self.shape.rotations[self.rotation % len(self.shape.rotations)]

    @property
    def shape_positions(self):
        positions = []
        for i, row in enumerate(self.current_form_of_shape):
            for j, column in enumerate(list(row)):
                if column == '0':
                    positions.append(self.__get_position(j, i))

        return positions

    def __get_position(self, j, i):
        return self.x + j - self.POS_OFFSET_X, self.y + i - self.POS_OFFSET_Y
