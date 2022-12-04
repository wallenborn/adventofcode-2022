import sys


# Input is items in elves' rucksacks, one line per rucksack.
# Each letter represents an item. Elves are grouped in groups
# of three elves each. Find the intersection
# of the sets of letters in each group. Letters
# are assigned numbers (priorities), find the sum
# of all the priorities for all letters in the intersections
# of all elves.
def main():
    if len(sys.argv) < 2:
        print ("Usage: advent-03-1.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    with open(filename) as file:
        sum_of_priorities = 0
        for line1, line2, line3 in chunks_of(size=3, iterator=file):
            letters1 = set(list(line1.rstrip()))
            letters2 = set(list(line2.rstrip()))
            letters3 = set(list(line3.rstrip()))
            for c in list(letters1 & letters2 & letters3):
                sum_of_priorities += prio(c)
    print(sum_of_priorities)


# Priorities are:
#    Lowercase item types a through z have priorities 1 through 26.
#    Uppercase item types A through Z have priorities 27 through 52.
def prio(c):
    all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pos = all_chars.find(c)
    if pos == -1:
        print("Error: char " + c + " is not valid")
    return pos + 1


# Read input in groups.
# From: https://stackoverflow.com/questions/9707902/read-lines-from-huge-text-files-at-groups-of-4
def grouped(size, iterator):
    yield tuple(next(iterator) for _ in range(size))


# Read from iterator, n elements at a time
# https://stackoverflow.com/questions/6335839/python-how-to-read-n-number-of-lines-at-a-time
def chunks_of(size, iterator):
    try:
        while True:
            yield [next(iterator) for j in range(0, size)]
    except StopIteration:
        return


if __name__ == '__main__':
    main()
