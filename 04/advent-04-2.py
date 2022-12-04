import sys

# Elves are assigned ranges, input is ranges for an elf pair
# Find the number of elf pairs where the ranges overlap
def main():
    if len(sys.argv) < 2:
        print ("Usage: advent-04-1.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    with open(filename) as file:
        result = 0
        for line in file:
            [left_str, right_str] = line.rstrip().split(',')
            left = list(map(lambda s: int(s), left_str.split('-')))
            right = list(map(lambda s: int(s), right_str.split('-')))
            if overlaps(left, right):
                result += 1
        print(result)


def overlaps(left, right):
    return not (max(left) < min(right) or max(right) < min(left))


if __name__ == '__main__':
    main()
