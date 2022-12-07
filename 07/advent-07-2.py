import re
import sys
from node import Node


# In a directory structure, find the smallest
# directory big enough to free enough space when deleted
def main():
    if len(sys.argv) < 2:
        print("Usage: advent-07-2.py <inputfile>")
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

        # Total disk size is 70MB, and we need
        # 30MB of free space
        disk_size = 70000000
        total_required = 30000000
        total_used = root.get_size()
        total_free = disk_size - total_used
        # We need to free up this much additional space
        additional_required = total_required - total_free
        # List all dirs and sort them by the space they use
        all_dirs = traverse(root)
        sorted_dirs = sorted(all_dirs, key=lambda x: x.get_size())
        # Find the first dir that's big enough to free a total of 30MB
        for d in sorted_dirs:
            if d.get_size() >= additional_required:
                print(d.get_size())
                break


def traverse(node):
    res = []
    if node and node.type == Node.DIRECTORY:
        res.append(node)
        for n in node.nodes:
            res = res + traverse(n)
    return res


if __name__ == '__main__':
    main()
