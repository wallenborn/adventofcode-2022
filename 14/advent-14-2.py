import re
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: advent-14-2.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    data = dict()
    min_x = 500
    max_x = 500
    min_y = 0
    max_y = 0
    start_x = 500
    start_y = 0
    with open(filename) as file:
        for line in file:
            s = line.rstrip()
            points = s.split("->")
            xx = None
            yy = None
            for p in points:
                [x, y] = parse(p)
                min_x = min(x, min_x)
                max_x = max(x, max_x)
                min_y = min(y, min_y)
                max_y = max(y, max_y)
                if xx is None and yy is None:
                    xx = x
                    yy = y
                    continue
                if y == yy and x < xx:
                    for i in range(x, xx + 1):
                        data[key(i, y)] = "#"
                elif y == yy and x > xx:
                    for i in range(xx, x + 1):
                        data[key(i, y)] = "#"
                elif x == xx and y < yy:
                    for j in range(y, yy + 1):
                        data[key(x, j)] = "#"
                elif x == xx and y > yy:
                    for j in range(yy, y + 1):
                        data[key(x, j)] = "#"
                xx = x
                yy = y
    min_x -= 1
    max_x += 1
    max_y += 2
    for x in range(min_x, max_x + 1):
        data[key(x, max_y)] = "#"
    #print_world_map(data, min_x, max_x, min_y, max_y)
    #print("World map: min_x: %d, max_x: %d, min_y: %d: max_y: %d" % (min_x, max_x, min_y, max_y))
    sand = 0
    while True:
        x = start_x
        y = start_y
        while True:
            if y == max_y - 1 and x == min_x:
                data[key(x - 1, y + 1)] = "#"
                min_x -= 1
            elif y == max_y -1 and x == max_x:
                data[key(x + 1, y + 1)] = "#"
                max_x += 1
            if key(x, y + 1) not in data:
                y += 1
            elif key(x - 1, y + 1) not in data:
                x -= 1
                y += 1
            elif key(x + 1, y + 1) not in data:
                x += 1
                y += 1
            else:
                break
        data[key(x, y)] = "o"
        sand += 1
        if x == start_x and y == start_y:
            break
    #print_world_map(data, min_x, max_x, min_y, max_y)
    print(sand)


def parse(p):
    m = re.match("\\D*(\\d+),(\\d+)\\D*", p)
    return list(map(int,m.groups()))


def key(x, y):
    return str(x) + "," + str(y)


def print_world_map(data, min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y + 1):
        s = ""
        for x in range(min_x, max_x + 1):
            s += data.get(key(x, y), '.')
        print(s)


if __name__ == '__main__':
    main()