class BucketFill:
    def __init__(self, x, y, color, canvas):
        self._coordinates = []
        self._color = color
        self.canvas = canvas
        self.canvas.validate_coordinate(x, y)
        self._bucket_fill(x, y)
        self._draw_fill()

    def _bucket_fill(self, x, y):
        if (x <= 0 or x > self.canvas.width or y <= 0 or
                y > self.canvas.height or self.canvas.matrix[y][x] != ' '):
            return
        if (x, y) in self._coordinates:
            return
        self._coordinates.append((x, y))
        self._bucket_fill(x - 1, y)
        self._bucket_fill(x + 1, y)
        self._bucket_fill(x, y + 1)
        self._bucket_fill(x, y - 1)

    def _draw_fill(self):
        self.canvas.coordinates = self._coordinates
        self.canvas.draw(shape=self._color)
        self.canvas.print_canva()
