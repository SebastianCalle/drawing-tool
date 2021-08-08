from factory.commad_line import ICommandLine
from utils.file_handler import FileHandler



if __name__ == '__main__':
    file = FileHandler()
    commands = file.read_file()
    ICommandLine(file.commands)
