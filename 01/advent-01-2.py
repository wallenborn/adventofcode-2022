import sys


# Input is calories of snacks carried by elves
# grouped by elves, with empty line as delimiter
# Find the sum of the 3 highest amounts of any elf
def main():
    if len(sys.argv) < 2:
        print("Usage: advent-01-2.py <inptfile>")
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
    elf.sort(reverse=True)
    print(sum(elf[:3]))


if __name__ == '__main__':
    main()
