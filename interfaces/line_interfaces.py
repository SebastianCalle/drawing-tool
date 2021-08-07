from drawing_tools.line import Line


class ILine:
    def __init__(self, command, instances):
        self.instance = Line(int(command[1]), int(command[2]), int(command[3]), int(command[4]), instances['C'].instance)
