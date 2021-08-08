from interfaces.bucket_file_interfaces import IBucketFill
from interfaces.canvas_interface import ICanvas
from interfaces.line_interfaces import ILine
from interfaces.rectangle_interfaces import IRectangle


class ICommandLine:

    my_commands = {
        'C': ICanvas,
        'R': IRectangle,
        'L': ILine,
        'B': IBucketFill
    }

    def __init__(self, list_commands):
        self._commands = list_commands
        self._instances = {}
        self._execute_commands()

    def _execute_commands(self):

        if self._commands:
            if self._commands[0][0].upper() != 'C':
                raise ValueError('First command must be create a canvas C w h')

            for command in self._commands:
                self._instances[command[0]] = self.my_commands[command[0]](command, self._instances)