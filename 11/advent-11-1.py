import sys
from monkey import Monkey


def main():
    if len(sys.argv) < 2:
        print("Usage: advent-11-1.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    monkeys = list()
    with open(filename) as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = file.readline()
            m = Monkey(line)
            line = file.readline()
            m.set_inspector_function(line)
            line = file.readline()
            m.set_test_function(line)
            line = file.readline()
            m.set_if_true(line)
            line = file.readline()
            m.set_if_false(line)
            line = file.readline()
            monkeys.append(m)

    for i in range(20):
        for m in monkeys:
            items = m.items
            m.items = list()
            for item in items:
                x = m.inspect(item)
                x = m.relax(x)
                monkeys[m.throw_to(x)].items.append(x)

    inspections = sorted(list(map(lambda m: m.num_inspections, monkeys)), reverse=True)
    print(inspections[0] * inspections[1])


if __name__ == '__main__':
    main()
