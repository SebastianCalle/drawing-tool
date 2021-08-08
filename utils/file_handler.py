from utils.validators import is_valid_command
import os


class FileHandler:

    def __init__(self):
        self.commands = []
        self._validate_file_exists()

    @classmethod
    def write_file(cls, char):
        with open('output.txt', 'a') as the_file:
            the_file.write(char)

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


    def _validate_file_exists(self):
        if os.path.exists("output.txt"):
            os.remove("output.txt")