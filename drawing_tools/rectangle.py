

class Rectangle:

    def __init__(self, x1, y1, x2, y2, canvas):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.canvas = canvas
        self._coordinates = []
        self._draw_rectangle()

    def _draw_rectangle(self):
        self.canvas.validate_coordinates(self._x1, self._y1, self._x2, self._y2)
        # print(f'({coor1}, {coor2})')
        for y in range(self._y1, self._y2 + 1):
            for x in range(self._x1, self._x2 + 1):
                # print(f'{x}, {y} | ({self._x1}, {self._y1}) | ({self._x2}, {self._y2})')
                if x == self._x1 or y == self._y1 or x == self._x2 or y == self._y2:
                    self._coordinates.append((x, y))
        # print('cor', [cor for cor in self._coordinates])
        self.canvas.coordinates = self._coordinates
        self.canvas.draw()
        self.canvas.print_canva()
