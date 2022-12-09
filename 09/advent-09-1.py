from rope import Rope
import sys


# Simulate a rope as a number of nodes that must always be adjacent.
# Initially, all nodes are at (0,0), but then the first node (the head)
# gets moved according to the input directives. All other points then
# follow such that the adjacency is maintained. Find the number of
# points that the last node (the tail) visits along the way
def main():
    if len(sys.argv) < 2:
        print("Usage: advent-09-1.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    with open(filename) as file:
        # This rope only consists of a head and a tail
        rope = Rope(2)
        for line in file:
            [direction, steps] = line.split(" ")
            steps = int(steps)
            if direction == "U":
                for i in range(steps):
                    rope.head_up()
            elif direction == "R":
                for i in range(steps):
                    rope.head_right()
            elif direction == "D":
                for i in range(steps):
                    rope.head_down()
            elif direction == "L":
                for i in range(steps):
                    rope.head_left()
    print(len(rope.visited))


if __name__ == '__main__':
    main()
