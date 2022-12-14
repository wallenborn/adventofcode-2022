import sys


# Elves are assigned ranges, input is ranges for an elf pair
# Find the number of elf pairs where one range contains the other
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
            if contains(left, right) or contains(right, left):
                result += 1
        print(result)


def contains(left, right):
    return left[0] <= right[0] and right[1] <= left[1]


if __name__ == '__main__':
    main()
