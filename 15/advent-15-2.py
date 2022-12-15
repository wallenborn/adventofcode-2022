import sys
from sensor import Sensor


# Find the only point in the grid that's not in the
# range of any sensor
def main():
    if len(sys.argv) < 6:
        print("Usage: advent-15-1.py <inputfile> <min_x> <max_x> <min_y> <max_y>")
        sys.exit(1)
    filename = sys.argv[1]
    min_x = int(sys.argv[2])
    max_x = int(sys.argv[3])
    min_y = int(sys.argv[4])
    max_y = int(sys.argv[5])

    sensors = list()
    with open(filename) as file:
        for line in file:
            s = Sensor(line)
            sensors.append(s)

    for row_number in range(min_y, max_y + 1):
        pos = min_x
        while pos < max_x:
            # print("I am here: %d,%d" % (pos, row_number))
            sensors_in_range = find_sensors_in_range(sensors, pos, row_number)
            if len(sensors_in_range) == 0:
                # Bingo!
                print(pos * 4000000 + row_number)
                break
            else:
                new_pos = min(max_x, find_next_pos(sensors_in_range, pos, row_number))
                pos = new_pos


def find_next_pos(sensors, x, y):
    max_x = None
    for s in sensors:
        candidate_x = s.x + s.dx(y)
        if max_x is None or candidate_x > max_x:
            max_x = candidate_x
    return max_x + 1


def find_sensors_in_range(sensors, x, y):
    return list(filter(lambda s: s.manhattan_dist(x, y) <= s.dist, sensors))


if __name__ == '__main__':
    main()