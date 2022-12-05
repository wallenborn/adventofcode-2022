import re
import sys


# Move items from stacks to other stacks. Input has a header
# section describing the initial stack configuration, then a
# blank line and an instruction section, with 1 instruction
# per line. Find the list of elements on top of the stacks
# after executing all the instructions
def main():
    if len(sys.argv) < 2:
        print ("Usage: advent-05-1.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    with open(filename) as file:
        read_header = True
        header = list()
        for line in file:
            if read_header and not line.isspace():
                header.insert(0, line.rstrip())
            elif read_header and line.isspace():
                stacks = initialize_stacks(header)
                read_header = False
            else:
                cmd = re.match("move (\\d+) from (\\d+) to (\\d+)", line)
                [num, from_stack, to_stack] = list(cmd.groups())
                for i in range(int(num)):
                    # move items one at a time
                    item = stacks[int(from_stack)-1].pop()
                    stacks[int(to_stack)-1].append(item)
    result = ''
    for s in stacks:
        result += s.pop()
    print(result)


# First line of header gives the number of stacks
# Each following line contains the elements for this
# level
def initialize_stacks(header):
    stacks = list()
    first_line = header.pop(0)
    matches = re.findall("(\\d+)", first_line)
    num_stacks = len(matches)
    for i in range(num_stacks):
        stacks.append(list())
    for line in header:
        for i in range(num_stacks):
            # Assume we have <10 stacks
            s = line[4*i+1:4*i+2]
            if s and not s.isspace():
                stacks[i].append(s)
    return stacks


if __name__ == '__main__':
    main()
