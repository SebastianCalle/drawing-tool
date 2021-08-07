from abc import ABC

from drawing_tools.bucket_fill import BucketFill
from drawing_tools.rectangle import Rectangle
from drawing_tools.line import Line


class Canvas(ABC):
    """ Class to provide canvas for drawing tool."""

    def __init__(self, width, height, coordinates=[]):
        self._width = width
        self._height = height
        self._matrix = []
        self._coordinates = coordinates
        self._shape = 'x'
        self.create_canvas()

    @property
    def matrix(self):
        return self._matrix

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, color):
        self._shape = color

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coors):
        self._coordinates = coors

    def create_canvas(self):
        for y in range(0, self._height + 2):
            row = []
            for x in range(0, self._width + 2):
                if y == 0 or y == self._height + 1:
                    row.append('-')
                elif x == 0 or x == self._width + 1:
                    row.append('|')
                else:
                    row.append(f' ')
            self._matrix.append(row)
        self.draw()
        self.print_canva()

    def draw(self, shape='x'):
        """Draw the canvas."""

        for x in range(len(self._matrix[0])):
            for y in range(len(self._matrix)):
                if (x, y) in self._coordinates and self._matrix[y][x] == ' ':
                     self._matrix[y][x] = shape

    def print_canva(self):
        for x in range(len(self._matrix)):
            for y in range(len(self._matrix[0])):
                print(self._matrix[x][y], end='')
            print('')

    def validate_coordinates(self,x1,y1,x2,y2):
        if x1 > self._width or x2 > self._width:
            raise ValueError('Coordinates pass the grid')
        if y1 > self._height or y2 > self._height:
            raise ValueError('Coordinates pass the grid')

    def validate_coordinate(self, x, y):
        if x >  self._width or y > self._height:
            print( f'x, y {x}, {y} ')
            raise ValueError('Coordinates pass the grid')

if __name__ == '__main__':
    canva = Canvas(20, 4)
    line = Line(5,2,1,2,canva)
    # line = [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2)]
    #canva.coordinates =
    line2 = Line(6,2,6,4,canva)
    # canva.coordinates = line2.make_line()
    rectangle = Rectangle(16,1,20,3, canva)
    color = 'R'
    bucket_fill = BucketFill(12,2, color, canva)

