import sys
from sensor import Sensor


# Find the number of points in row <rownumber> that cannot be the
# position of a known beacon, i.e. count the points that are
# - not a beacon position,
# - and not closer to any sensor than their beacon distance
def main():
    if len(sys.argv) < 3:
        print("Usage: advent-15-1.py <inputfile> <rownumber>")
        sys.exit(1)
    filename = sys.argv[1]
    row_number = int(sys.argv[2])

    sensors = list()
    min_x = None
    max_x = None
    with open(filename) as file:
        for line in file:
            s = Sensor(line)
            sensors.append(s)
            if min_x is None or min_x > s.x - s.dist:
                min_x = s.x - s.dist
            if max_x is None or max_x < s.x + s.dist:
                max_x = s.x + s.dist
    # print("Scanning row %d from %d to %d" % (row_number, min_x, max_x))
    # Brute force: test all points
    # score = 0
    # for x in range(min_x, max_x + 1):
    #     # Are we close to any sensor?
    #     for s in sensors:
    #         if s.manhattan_dist(x, row_number) <= s.dist:
    #             # print("Position %d cannot have a beacon" % (x))
    #             score += 1
    #             break
    #     # Are we a beacon position?
    #     for s in sensors:
    #         if x == s.beacon_x and row_number == s.beacon_y:
    #             score -= 1
    #             break
    # print(score)
    # Better algorithm: scan the row faster
    score = 0
    pos = min_x
    while pos < max_x:
        # print("I am here: %d,%d" % (pos, row_number))
        if not in_range(sensors, pos, row_number):
            # print("Not in range")
            s = find_next_sensor(sensors, pos, row_number)
            if s is None:
                break
            # print("Next sensor is at %d,%d, dist %d" % (s.x, s.y, s.dist))
            pos = s.x - s.dx(row_number)
            # print("Next pos is %d" % pos)
        else:
            # print("In range")
            s = find_current_sensor(sensors, pos, row_number)
            # print("Current sensor is at %d,%d, dist %d" % (s.x, s.y, s.dist))
            new_pos = s.x + s.dx(row_number) + 1
            score += new_pos - pos
            score -= count_beacons(sensors, pos, new_pos, row_number)
            pos = new_pos
            # print("Next pos is %d" % pos)
    print(score)


def count_beacons(sensors, min_x, max_x, y):
    beacons = dict()
    for s in sensors:
        if s.beacon_y == y and min_x <= s.beacon_x < max_x:
            # print("Found beacon at %d,%d" % (s.beacon_x, s.beacon_y))
            beacons[s.beacon_x] = True
    return len(beacons)


def find_current_sensor(sensors, x, y):
    max_x = None
    sensor = None
    for s in sensors:
        # Are we in this sensor's range?
        if s.manhattan_dist(x, y) > s.dist:
            continue
        candidate_x = s.x + s.dx(y)
        if max_x is None or candidate_x > max_x:
            max_x = candidate_x
            sensor = s
    return sensor


def find_next_sensor(sensors, x, y):
    min_x = None
    sensor = None
    for s in sensors:
        # Only look ahead, skip sensors behind us
        if s.x < x:
            continue
        # Also skip sensors that are to far away vertically
        if abs(s.y - y) > s.dist:
            continue
        candidate_x = s.x - s.dx(y)
        if min_x is None or candidate_x < min_x:
            min_x = candidate_x
            sensor = s
    return sensor


def in_range(sensors, x, y):
    for s in sensors:
        if s.manhattan_dist(x, y) <= s.dist:
            return True
    return False


if __name__ == '__main__':
    main()