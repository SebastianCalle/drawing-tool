from validators import is_valid_command


class FileHandler:

    def __init__(self):
        self.commands = []

    def read_file(self):

        with open('input.txt', 'r') as file:
            for line in file:
                command = line
                if line.endswith('\n'):
                    command = line[:-1]
                if is_valid_command(command):
                    self.commands.append(command.split(' '))
                else:
                    raise ValueError('File not valid')

    def writh_file(self):
