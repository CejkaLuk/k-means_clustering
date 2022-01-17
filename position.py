from math import sqrt, pow


class Position:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def print(self):
        print(f'({self.x}, {self.y})')

    def distance_to_pos(self, pos) -> float:
        """Return Euclidean distance from this position to a given position"""
        try:
            return sqrt(pow((self.x - pos.x), 2) + pow((self.y - pos.y), 2))
        except (AttributeError, TypeError):
            raise AssertionError(f'Input variable must be an instance of {type(self).__name__}')

