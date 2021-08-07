from drawing_tools.canva import Canvas

class ICanvas:
    def __init__(self, command, instances):
        self.instance = Canvas(int(command[1]), int(command[2]))
