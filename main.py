class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __getitem__(self, item):
        print('item', item)
        return self.x, self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

class DrawingTool:

    def __init__(self):
        self._commands = []
        self._width = 1
        self._height = 1
        self._coordinates= []
        self._bucket_fill_coordinates = []
        self.read_file()
        self._execute_commands()

    def _execute_commands(self):
        print('commands', self._commands)
        if self._commands:
            if self._commands[0][0].upper() != 'C':
                exit


        for command in self._commands:
            if command[0] == 'C' and self._commands.index(command) != 0: self._coordinates = []
                self._bucket_fill_coordinates = []

            if command[0] == 'C':
                self._width = int(command[1])
                self._height = int(command[2])
                self.draw_canvas()
            elif command[0] == 'L':
                coor1 = Coordinate(int(command[1]), int(command[2]))
                coor2 = Coordinate(int(command[3]), int(command[4]))
                self.draw_line(coor1, coor2)
                self.draw_canvas()
            elif command[0] == 'R':
                coor1 = Coordinate(int(command[1]), int(command[2]))
                coor2 = Coordinate(int(command[3]), int(command[4]))
                self.draw_rectangle(coor1, coor2)
                self.draw_canvas()
            elif command[0] == 'B':
                x = int(command[1])
                y = int(command[2])
                color = command[3]
                self.bucket_fill(x, y)
                self.draw_canvas(shape=color)



    def read_file(self):
        with open('input.txt', 'r') as file:
            for line in file:
                command = line
                if line.endswith('\n'):
                    command = line[:-1]
                if self._is_valid_command(command):
                    self._commands.append(command.split(' '))
                else:
                    raise ValueError('File not valid')

    def write_file(self):
        pass

    def is_valid_command(self, line):
        command = line.replace('\n', '').split(' ')
        if command[0].upper() == 'C' and len(command) == 3:
            self._width = int(command[1])
            self._height = int(command[2])
            return True
        elif command[0].upper() == 'L' and len(command) == 5:
            return True
        elif command[0].upper() == 'R' and len(command) == 5:
            return True
        elif command[0].upper() == 'B' and len(command) == 4:
            return True
        else:
            return False
        pass

    def validate_coordinates(self, coor1, coor2):
        if coor1.x > self._width or coor2.x > self._width:
            raise ValueError('Coordinates pass the grid')
        if coor1.y > self._height or coor2.y > self._height:
            raise ValueError('Coordinates pass the grid')

    def draw_canvas(self, shape='0'):
        print(f'shape: {shape}')
        for y in range(0, self._height + 2):
            for x in range(0, self._width + 2):
                if (x, y) in self._coordinates:
                    #print(f"(X, X)", end='')
                    print('x' , end='')
                elif (x, y) in self._bucket_fill_coordinates:
                    #print(f"({shape}, {shape})", end='')
                    print(shape, end='')
                elif y == 0 or y == self._height + 1:
                    print("-", end='')
                elif x == 0 or x == self._width + 1:
                    print("|", end='')
                else:
                    #print(f"({x}, {y})", end='')
                    #self._coordinates.append(Coordinate(int(x),int(y)))
                    print(' ', end='')
            print('')

    def draw_line(self, coor1, coor2):
        self.validate_coordinates(coor1, coor2)
        if (coor1.x, coor1.y) in self._bucket_fill_coordinates:
            self._bucket_fill_coordinates.remove((coor1.x, coor1.y))
        if (coor2.x, coor2.y) in self._bucket_fill_coordinates:
            self._bucket_fill_coordinates.remove((coor2.x, coor2.y))
        if coor1.x == coor2.x:
            if coor1.y < coor2.y:
                for y in range(coor1.y, coor2.y + 1):
                    coor_aux = Coordinate(coor1.x, y)
                    self._coordinates.append((coor_aux.x, coor_aux.y))
            elif coor1.y > coor2.y:
                for y in range(coor1.y, coor2.y - 1, -1):
                    coor_aux = Coordinate(coor1.x, y)
                    self._coordinates.append((coor_aux.x, coor_aux.y))
        elif coor1.y == coor2.y:
            if coor1.x < coor2.x:
                for x in range(coor1.x, coor2.x + 1):
                    coor_aux = Coordinate(x, coor1.y)
                    self._coordinates.append((coor_aux.x, coor_aux.y))
            if coor1.x > coor2.x:
                for x in range(coor1.x, coor2.x - 1, -1):
                    coor_aux = Coordinate(x, coor1.y)
                    self._coordinates.append((coor_aux.x, coor_aux.y))

        print('cor', [cor for cor in self._coordinates])


    def draw_rectangle(self, coor1, coor2):
        self.validate_coordinates(coor1, coor2)
        #print(f'({coor1}, {coor2})')
        for y in range(coor1.y, coor2.y + 1):
            for x in range(coor1.x, coor2.x + 1):
                #print(f'{x}, {y} | ({coor1.x}, {coor1.y}) | ({coor2.x}, {coor2.y})')
                if x == coor1.x or y == coor1.y or x == coor2.x or y == coor2.y:
                    self._coordinates.append((x,y))
        #print('cor', [cor for cor in self._coordinates])




    def bucket_fill(self, x, y):
        if (x <= 0 or x >= self._width or y <= 0 or
                y >= self._height + 1 or (x,y) in self._coordinates or
                (x,y) in self._bucket_fill_coordinates):
            return

            # Replace the color at (x, y)
        if (x,y) not in self._coordinates and (x,y) not in self._bucket_fill_coordinates and x > 0 and y > 0:
            #print(f"x: {x}, y:{y}")
            self._bucket_fill_coordinates.append((x,y))
        self.bucket_fill(x - 1, y)
        self.bucket_fill(x + 1, y)
        #print(f'down: x:{x}, y:{y}')
        self.bucket_fill(x, y + 1)
        self.bucket_fill(x, y - 1)
        # if (x, y) not in self._coordinates:
        #     self._bucket_fill_coordinates.append((x,y))
        # self.bucket_fill(x + 1, y)  # right
        # self.bucket_fill(x - 1, y)  # left
        # self.bucket_fill(x, y + 1)  # down
        # self.bucket_fill(x, y - 1)  # up
        # return


# class Canva:
#
#     _coordinates = []
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.create_canvas()
#
#     def draw_line(self, coor1, coor2):
#         pass
#
#
#     def create_canvas(self, shape='x'):
#
#         for y in range(0, self.height + 2):
#             for x in range(0, self.width + 2):
#                 if (x, y) in self._coordinates:
#                     print(shape, end='')
#                 elif y == 0 or y == self.height + 1:
#                     print("-", end='')
#                 elif x == 0 or x == self.width + 1:
#                     print("|", end='')
#                 else:
#                     print(f"({x}, {y})", end='')
#                     #print(' ', end='')
#             print('')
#


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    tool = DrawingTool()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()



