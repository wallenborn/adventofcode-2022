import functools
import json
import numpy
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: advent-13-2.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    packets = [ [[2]], [[6]] ]
    with open(filename) as file:
        while True:
            line = file.readline()
            if not line:
                break
            if line.isspace():
                continue
            packets.append(json.loads(line))
    sorted_packets = sorted(packets, key=functools.cmp_to_key(compare))
    print(find_index(sorted_packets, [[2]]) * find_index(sorted_packets, [[6]]))


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


def find_index(lst, candidate):
    for i, element in enumerate(lst):
        if compare(element, candidate) == 0:
            return i + 1
    return None


if __name__ == '__main__':
    main()
