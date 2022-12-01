import sys


def main():
    if (len(sys.argv) < 2):
        print ("Usage: advent-01-1.py <inptfile>")
        sys.exit(1)
    filename = sys.argv[1]
    print("Reading input from " + filename)
    elf = list()
    calories = 0
    with open(filename) as file:
        for line in file:
            if len(line.strip()) == 0:
                elf.append(calories)
                calories = 0
            else:
                calories += int(line)
        elf.append(calories)
    print(max(elf))


if __name__ == '__main__':
    main()
