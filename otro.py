import os
import re


class Draw:
    """
    Class draw on a canvas

    Canvas to initialize valid width and height(1,1)
    Supported draw vertical and horizontal lines in canvas
    Supported Bucket fill in canvas
    """

    def __init__(self):
        """ Instance of member class variable """
        self.canvas = []  # matrix contain width and height of canvas
        self.paint = ""  # used to show the canvas
        self.command = ""  # used to split console user input
        self.console = ""  # used to user input

    def validate(self):
        pattern_canvas = re.compile('[C] [1-9][0-9]? [1-9][0-9]?$')
        pattern_line = re.compile('[LR] [1-9][0-9]? [1-9][0-9]? [1-9][0-9]? [1-9][0-9]?$')
        pattern_fill = re.compile('[B] [1-9][0-9]? [1-9][0-9]? [a-z]$')

        if self.console == "Q":
            return True
        elif re.match(pattern_canvas, self.console):
            return True
        elif re.match(pattern_line, self.console):
            return True
        elif re.match(pattern_fill, self.console):
            return True
        else:
            raise Exception('Command {0} not valid!'.format(self.console))

    def new_canvas(self, w, h):
        """
        Create a new canvas
        :param int w: Width of canvas
        :param int h: Height of canvas
        """
        self.canvas = [[' ' for x in range(w)] for y in range(h)]

    def draw_line(self, x1, y1, x2, y2, character='x'):
        """
        Create Horizontal and vertical lines will be drawm using the 'x' character
        :param int x1: Start coordinate in axis x
        :param int x2: End coordinate in axis x
        :param int y1: Start coordinate in axis y
        :param int y2: End coordinate in axis y
        :param string character (default='x'): Character with which the line is drawn
        """
        if y1 == y2:
            for x in range(x1 - 1, x2):
                self.canvas[y2 - 1][x] = character
        elif x1 == x2:
            for y in range(y1 - 1, y2):
                self.canvas[y][x1 - 1] = character
        else:
            raise ValueError("The coordinates not correspond with a vertical or horizontal line")

    def flood_fill(self, x, y, color):
        """
        flood fill start point, using tails in the 4 directions
        :param int x: Start coordinate in axis x
        :param int y: Start coordinate in axis y
        :param string color: Character used for paint
        """
        fill = set()
        fill.add((x, y))

        while len(fill) != 0:
            (x, y) = fill.pop()
            if not self.canvas[y][x] == ' ':
                continue
            self.canvas[y][x] = color
            if x > 0:
                fill.add((x-1, y))
            if x < len(self.canvas[y]) - 1:
                fill.add((x+1, y))
            if y > 0:
                fill.add((x, y-1))
            if y < len(self.canvas) - 1:
                fill.add((x, y+1))

    def show_canvas(self):
        """ Show the canvas """
        for x in range(len(self.canvas)):
            for y in range(len(self.canvas[x])):
                self.paint += str(self.canvas[x][y])
            print('|' + self.paint + '|')
            self.paint = ""

    def canvas_control(self, console):
        """
        control to paint in canvas according to the user decision
        :param string console: Console input from user
        """
        self.console = console
        try:
            if self.validate() and self.console != "Q":
                self.command = self.console.split(" ")
                os.system("clear")
                if self.command[0] == 'C':
                    self.new_canvas(int(self.command[1]), int(self.command[2]))
                elif self.command[0] == 'L':
                    self.draw_line(int(self.command[1]), int(self.command[2]), int(self.command[3]),
                                   int(self.command[4]))
                elif self.command[0] == 'R':
                    self.draw_line(int(self.command[1]), int(self.command[2]), int(self.command[3]),
                                   int(self.command[2]))
                    self.draw_line(int(self.command[1]), int(self.command[4]), int(self.command[3]),
                                   int(self.command[4]))
                    self.draw_line(int(self.command[1]), int(self.command[2]), int(self.command[1]),
                                   int(self.command[4]))
                    self.draw_line(int(self.command[3]), int(self.command[2]), int(self.command[3]),
                                   int(self.command[4]))
                elif self.command[0] == 'B':
                    self.flood_fill(int(self.command[1]) - 1, int(self.command[2]) - 1, self.command[3])

                if self.paint == '':
                    self.show_canvas()

        except Exception as ex:
            print('Oops! The command {0} is not valid'.format(console))
            print(ex.args)

    def user_input(self):
        console = ""

        while console != "Q":
            console = input('Enter command: ')
            self.canvas_control(console)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi()
    canva = Draw()
    canva.user_input()

