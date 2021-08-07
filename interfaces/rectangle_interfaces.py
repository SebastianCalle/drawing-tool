from drawing_tools.rectangle import  Rectangle


class IRectangle:
    def __init__(self, command, instances):
        self.instance = Rectangle(int(command[1]), int(command[2]), int(command[3]), int(command[4]), instances['C'].instance)



