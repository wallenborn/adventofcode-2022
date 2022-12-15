import re


class Sensor:

    def __init__(self, line):
        m = re.match(".*Sensor at x=([\\-\\d]+), y=([\\-\\d]+): closest beacon is at x=([\\-\\d]+), y=([\\-\\d]+).*", line)
        [x, y, beacon_x, beacon_y] = m.groups()
        self.x = int(x)
        self.y = int(y)
        self.beacon_x = int(beacon_x)
        self.beacon_y = int(beacon_y)
        self.dist = self.manhattan_dist(self.beacon_x, self.beacon_y)

    def manhattan_dist(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

    def dx(self, y):
        return self.dist - abs(self.y - y)

    def dy(self, x):
        return self.dist - abs(self.x - x)
