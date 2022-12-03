import sys


# Input is items in elves' rucksacks, one line per rucksack.
# Left half is compartment 1, right is compartment 2.
# Each letter represents an item. Find the intersection
# of the sets of letters in the compartments. Letters
# are assigned numbers (priorities), find the sum
# of all the priorities for all letters in the intersections
# of all elves.
def main():
    if len(sys.argv) < 2:
        print ("Usage: advent-03-1.py <inptfile>")
        sys.exit(1)
    filename = sys.argv[1]

    with open(filename) as file:
        sumofpriorities = 0
        for line in file:
            rucksack = line.rstrip()
            left = rucksack[:len(rucksack)//2]
            right = rucksack[len(rucksack)//2:]
            letters_left = set(list(left))
            letters_right = set(list(right))
            for c in list(letters_left & letters_right):
                sumofpriorities += prio(c)
    print(sumofpriorities)


# Priorities are:
#    Lowercase item types a through z have priorities 1 through 26.
#    Uppercase item types A through Z have priorities 27 through 52.
def prio(c):
    allchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pos = allchars.find(c)
    if pos == -1:
        print("Error: char " + c + " is not valid" )
    return pos + 1


if __name__ == '__main__':
    main()
