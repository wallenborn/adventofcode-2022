class Node:

    DIRECTORY = 1
    FILE = 2

    def __init__(self, name, type):
        self.size = 0
        self.name = name
        self.type = type
        self.parent = None
        if type == Node.DIRECTORY:
            self.nodes = list();
        else:
            self.nodes = None

    def set_parent(self, node):
        self.parent = node

    def get_parent(self):
        return self.parent

    def set_size(self, size):
        self.size = size

    def get_size(self):
        if self.type == Node.DIRECTORY:
            return sum(s.get_size() for s in self.nodes)
        elif self.type == Node.FILE:
            return self.size

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def add_node(self, node):
        self.nodes.append(node)

    def get_nodes(self):
        return self.nodes;

    def find_node(self, name):
        for n in self.nodes:
            if name == n.get_name():
                return n
        return None
