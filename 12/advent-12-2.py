import sys
from node import Node


# Find the shortest path through a graph defined by
# the heights height map. Rules: beginning at S,
# move up, down, left or right, but only if the
# adjacent field is no more than one unit higher.
# Find the length of the shortest path from any
# point of height 1
def main():
    if len(sys.argv) < 2:
        print("Usage: advent-12-2.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    heights = list()
    with open(filename) as file:
        for i, line in enumerate(file):
            row = list()
            for j, ch in enumerate(list(line.rstrip())):
                if ch == "S":
                    n = Node(1)
                    n.row = i
                    n.col = j
                    row.append(n)
                elif ch == "E":
                    n = Node(26)
                    n.row = i
                    n.col = j
                    n.distance = 0
                    n.predecessor = n
                    row.append(n)
                else:
                    n = Node(ord(ch) - 96)
                    n.row = i
                    n.col = j
                    row.append(n)
            heights.append(row)

    # Dijkstra's algorithm in reverse to find the shortest path
    # by enumerating the distance from end for all
    # neighbours of the point closest to it
    while True:
        n = find_nearest_unvisited_node(heights)
        if n is None:
            break
        n.visited = True
        if n.row > 0:
            m = heights[n.row - 1][n.col]
            if not m.visited and m.height >= n.height - 1 and (m.distance is None or m.distance > n.distance + 1):
                m.distance = n.distance + 1
                m.predecessor = n
        if n.row < len(heights) - 1:
            m = heights[n.row + 1][n.col]
            if not m.visited and m.height >= n.height - 1 and (m.distance is None or m.distance > n.distance + 1):
                m.distance = n.distance + 1
                m.predecessor = n
        if n.col > 0:
            m = heights[n.row][n.col - 1]
            if not m.visited and m.height >= n.height - 1 and (m.distance is None or m.distance > n.distance + 1):
                m.distance = n.distance + 1
                m.predecessor = n
        if n.col < len(heights[0]) - 1:
            m = heights[n.row][n.col + 1]
            if not m.visited and m.height >= n.height - 1 and (m.distance is None or m.distance > n.distance + 1):
                m.distance = n.distance + 1
                m.predecessor = n
    # Now we loop over all nodes, and find the shortest
    # distance for any node of height 1
    shortest_distance = None
    for row in heights:
        for col in row:
            if col.height == 1 and col.distance is not None and shortest_distance is None:
                shortest_distance = col.distance
            elif col.height == 1 and col.distance is not None and col.distance < shortest_distance:
                shortest_distance = col.distance
    print(shortest_distance)


def find_nearest_unvisited_node(heights):
    this_node = None
    for row in heights:
        for col in row:
            if not col.visited and col.distance is not None and this_node is None:
                this_node = col
            elif not col.visited and col.distance is not None and col.distance < this_node.distance:
                this_node = col
    return this_node


def print_distances(heights):
    for row in heights:
        s = ""
        for col in row:
            if col.distance is None:
                s += "..."
            else:
                s += "{dist:3d}".format(dist=col.distance)
        print(s)


def print_path(heights, end_node):
    output = list()
    for row in heights:
        r = list()
        for col in row:
            r.append(".")
        output.append(r)
    this_node = end_node
    prev_node = end_node.predecessor
    while this_node != prev_node:
        output[this_node.row][this_node.col] = "*"
        this_node = prev_node
        prev_node = prev_node.predecessor
    output[this_node.row][this_node.col] = "*"
    for r in output:
        print("".join(r))


if __name__ == '__main__':
    main()
