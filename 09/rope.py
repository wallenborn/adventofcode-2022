class Rope:

    def __init__(self, length):
        self.nodes = list()
        for i in range(length):
            self.nodes.append([0,0])
        self.visited = dict({"0|0": True})

    def head_up(self):
        self.nodes[0][1] += 1
        for p in range(1, len(self.nodes)):
            self.nodes[p] = self.follow(self.nodes[p-1], self.nodes[p])
        key = str(self.nodes[-1][0]) + "|" + str(self.nodes[-1][1])
        self.visited[key] = True

    def head_right(self):
        self.nodes[0][0] += 1
        for p in range(1, len(self.nodes)):
            self.nodes[p] = self.follow(self.nodes[p-1], self.nodes[p])
        key = str(self.nodes[-1][0]) + "|" + str(self.nodes[-1][1])
        self.visited[key] = True

    def head_down(self):
        self.nodes[0][1] -= 1
        for p in range(1, len(self.nodes)):
            self.nodes[p] = self.follow(self.nodes[p-1], self.nodes[p])
        key = str(self.nodes[-1][0]) + "|" + str(self.nodes[-1][1])
        self.visited[key] = True

    def head_left(self):
        self.nodes[0][0] -= 1
        for p in range(1, len(self.nodes)):
            self.nodes[p] = self.follow(self.nodes[p-1], self.nodes[p])
        key = str(self.nodes[-1][0]) + "|" + str(self.nodes[-1][1])
        self.visited[key] = True

    def follow(self, x, y):
        d = self.distance(x, y)
        result = y
        if d <= 1:
            return result
        if x[0] > y[0]:
            y[0] += 1
        elif x[0] < y[0]:
            y[0] -= 1
        if x[1] > y[1]:
            y[1] += 1
        elif x[1] < y[1]:
            y[1] -= 1
        return y

    @staticmethod
    def distance(x, y):
        return max(abs(x[0]-y[0]), abs(x[1]-y[1]))
