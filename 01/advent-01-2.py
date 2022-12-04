import sys


# Input is calories of snacks carried by elves
# grouped by elves, with empty line as delimiter
# Find the sum of the 3 highest amounts of any elf
def main():
    if len(sys.argv) < 2:
        print("Usage: advent-01-2.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    with open(filename) as file:
        # Initialize one elf
        elf = [0]
        for line in file:
            if line.isspace():
                # Empty line -> new elf
                elf.append(0)
            else:
                # Add calories to this elf
                elf[-1] += int(line)

    # Print result
    elf.sort()
    print(sum(elf[-3:]))


if __name__ == '__main__':
    main()
