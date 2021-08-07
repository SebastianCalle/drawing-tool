from drawing_tools.bucket_fill import BucketFill


class IBucketFill:
    def __init__(self, command, instances):
        self.instance = BucketFill(int(command[1]), int(command[2]), command[3], instances['C'].instance)
