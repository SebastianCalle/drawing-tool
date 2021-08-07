class Line:

    def __init__(self, x1, y1, x2, y2, canvas):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.canvas = canvas
        self._coordinates = []
        self._draw_line()

    def _draw_line(self):
        self.canvas.validate_coordinates(self._x1, self._y1, self._x2, self._y2)

        if (self._x1, self._y1) in self.canvas.coordinates:
            self.canvas.coordinates.remove((self._x1, self._y1))
        if (self._x2, self._y2) in self.canvas.coordinates:
            self.canvas.coordinates.remove((self._x2, self._y2))

        if self._x1 == self._x2:
            if self._y1 < self._y2:
                for y in range(self._y1, self._y2 + 1):
                    self._coordinates.append((self._x1, y))
            elif self._y1 > self._y2:
                for y in range(self._y1, self._y2 - 1, -1):
                    self._coordinates.append((self._x1, y))
        elif self._y1 == self._y2:
            if self._x1 < self._x2:
                for x in range(self._x1, self._x2 + 1):
                    self._coordinates.append((x, self._y1))
            if self._x1 > self._x2:
                for x in range(self._x1, self._x2 - 1, -1):
                    self._coordinates.append((x, self._y1))

        self.canvas.coordinates = self._coordinates
        self.canvas.draw()
        self.canvas.print_canva()
