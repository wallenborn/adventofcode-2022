class Node:

    def __init__(self, height):
        self.height = height
        self.distance = None
        self.predecessor = None
        self.visited = False
        self.row = None
        self.col = None
