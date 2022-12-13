import json
import numpy
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: advent-13-1.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    idx = 0
    sum = 0
    with open(filename) as file:
        while True:
            line1 = file.readline()
            if not line1:
                break
            line2 = file.readline()
            file.readline()
            idx += 1
            left = json.loads(line1)
            right = json.loads(line2)
            cmp = compare(left, right)
            #print("Index: %d, Compare: %d" % (idx, cmp))
            if cmp < 0:
                sum += idx
    print(sum)


def compare(left, right):
    min_len = min(len(left), len(right))
    for i in range(0, min_len):
        ll = left[i]
        rr = right[i]
        if isinstance(ll, int) and isinstance(rr, int):
            cmp = numpy.sign(ll - rr)
        elif isinstance(ll, list) and isinstance(rr, list):
            cmp = compare(ll, rr)
        elif isinstance(ll, int) and isinstance(rr, list):
            cmp = compare([ll], rr)
        elif isinstance(ll, list) and isinstance(rr, int):
            cmp = compare(ll, [rr])
        else:
            print("Unknown type(s): " + type(ll) + ", " + type(rr))
        if cmp != 0:
            return cmp
    if len(left) > min_len:
        return 1
    elif len(right) > min_len:
        return -1
    else:
        return 0


if __name__ == '__main__':
    main()
