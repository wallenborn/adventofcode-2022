import re
import sys
from node import Node


# In a directory structure, find directories whose
# total size is smaller or equal than 100kB, and sum their sizes
def main():
    if len(sys.argv) < 2:
        print("Usage: advent-07-1.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    with open(filename) as file:
        root = Node("/", Node.DIRECTORY)
        for line in file:
            s = line.rstrip()
            mc = re.match("\\$\\s+cd\\s+([a-zA-Z\\.]+)", s)
            md = re.match("dir\\s+([a-zA-Z]+)", s)
            mf = re.match("(\\d+)\\s+([a-zA-Z\\.]+)", s)
            if s == "$ cd /":
                current_node = root
            elif mc:
                [name] = mc.groups()
                if name == "..":
                    current_node = current_node.get_parent()
                else:
                    this_dir = current_node.find_node(name)
                    if this_dir is None:
                        print("Dir does not exist: %s" % (name))
                    else:
                        current_node = this_dir
            elif md:
                [name] = md.groups()
                this_dir = Node(name, Node.DIRECTORY)
                this_dir.set_parent(current_node)
                current_node.add_node(this_dir)
            elif mf:
                [size, name] = mf.groups()
                this_file = Node(name, Node.FILE)
                this_file.set_size(int(size))
                current_node.add_node(this_file)
            elif s == "$ ls":
                pass

        # Sum up the sizes
        total_size = 0
        all_nodes = traverse(root)
        for n in all_nodes:
            # only count directories with a total
            # size of <= 100kB
            if n.get_size() <= 100000:
                total_size += n.get_size()
        print(total_size)


def traverse(node):
    res = []
    if node and node.type == Node.DIRECTORY:
        res.append(node)
        for n in node.nodes:
            res = res + traverse(n)
    return res


if __name__ == '__main__':
    main()
