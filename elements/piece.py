from random import choice
from content.shape import Shape


class Piece:
    POS_OFFSET_X = 2
    POS_OFFSET_Y = 3

    def __init__(self, x, y, shape: Shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.rotation = 0
        self.prev_x = x
        self.prev_y = y
        self.prev_rotation = 0

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
        self.rotation -= 1

    def undo_action(self):
        self.x = self.prev_x
        self.y = self.prev_y
        self.rotation = self.prev_rotation

    def perform_action(self):
        self.prev_x = self.x
        self.prev_y = self.y
        self.prev_rotation = self.rotation

    @property
    def is_in_the_field(self):
        return self.y > 0

    @property
    def current_form_of_shape(self):
        return self.shape.rotations[self.rotation % len(self.shape.rotations)]

    @property
    def shape_positions(self):
        return [self.__get_position(cell_num, row_num) for cell_num, row_num in self.shape_iterator()]

    def shape_iterator(self):
        for row_num, row in enumerate(self.current_form_of_shape):
            for cell_num, cell in enumerate(list(row)):
                if cell == '0':
                    yield cell_num, row_num

    def __get_position(self, j, i):
        return self.x + j - self.POS_OFFSET_X, self.y + i - self.POS_OFFSET_Y
