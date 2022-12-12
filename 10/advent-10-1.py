import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: advent-10-1.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    total_signal_strength = 0
    with open(filename) as file:
        x = 1
        cycle = 0
        for line in file:
            if "noop" == line.rstrip():
                cycle += 1
                total_signal_strength += signal_strength(cycle, x)
            else:
                [cmd, amount] = line.split(" ")
                amount = int(amount)
                cycle += 1
                total_signal_strength += signal_strength(cycle, x)
                cycle += 1
                total_signal_strength += signal_strength(cycle, x)
                x += amount
    print(total_signal_strength)


def signal_strength(cycle, x):
    if cycle == 20 \
            or cycle == 60 \
            or cycle == 100 \
            or cycle == 140 \
            or cycle == 180 \
            or cycle == 220:
        return cycle * x
    else:
        return 0


if __name__ == '__main__':
    main()
