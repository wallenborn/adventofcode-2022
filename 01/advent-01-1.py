import sys


# Input is calories of snacks carried by elves
# grouped by elves, with empty line as delimiter
# Find the maximum amount of calories any elf is carrying
def main():
    if len(sys.argv) < 2:
        print ("Usage: advent-01-1.py <inptfile>")
        sys.exit(1)
    filename = sys.argv[1]

    with open(filename) as file:
        elf = [0]
        for line in file:
            if len(line.strip()) != 0:
                # Add calories to this elf
                elf[-1] += int(line)
            else:
                # Empty line -> new elf
                elf.append(0)

    # Print result
    print(max(elf))


if __name__ == '__main__':
    main()
