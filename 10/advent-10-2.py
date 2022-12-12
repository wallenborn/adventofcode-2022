import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: advent-10-2.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    crt = [[" "] * 40,
           [" "] * 40,
           [" "] * 40,
           [" "] * 40,
           [" "] * 40,
           [" "] * 40]

    with open(filename) as file:
        x = 1
        cycle = 0
        for line in file:
            if "noop" == line.rstrip():
                [row, col] = position(cycle)
                if col == x - 1 or col == x or col == x + 1:
                    crt[row][col] = "#"
                else:
                    crt[row][col] = "."
                print("%s: cycle %d, x is %d" % (line.rstrip(), cycle, x))
                cycle += 1
            else:
                [cmd, amount] = line.split(" ")
                amount = int(amount)
                [row, col] = position(cycle)
                if col == x - 1 or col == x or col == x + 1:
                    crt[row][col] = "#"
                else:
                    crt[row][col] = "."
                cycle += 1
                [row, col] = position(cycle)
                if col == x - 1 or col == x or col == x + 1:
                    crt[row][col] = "#"
                else:
                    crt[row][col] = "."
                cycle += 1
                x += amount
    print_screen(crt)


def print_screen(crt):
    print("----------------------------------------")
    for i in range(len(crt)):
        print("".join(crt[i]))
    print("----------------------------------------")


def position(x):
    col = x % 40
    row = int((x - col) / 40)
    return [row, col]


if __name__ == '__main__':
    main()
