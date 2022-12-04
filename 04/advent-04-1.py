import sys


def main():
    if len(sys.argv) < 2:
        print ("Usage: advent-04-1.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    with open(filename) as file:
        result = 0
        for line in file:
            [left_str, right_str] = line.rstrip().split(',')
            left = left_str.split('-')
            right = right_str.split('-')
            if contains(left, right) or contains(right, left):
                result += 1
        print(result)


def contains(left, right):
    return int(left[0]) <= int(right[0]) and int(right[1]) <= int(left[1])


if __name__ == '__main__':
    main()
