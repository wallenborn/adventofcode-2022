import numpy as np
import sys


# Given an array of tree heights, find how many trees
# are visible from outside the forest, i.e. how many
# trees have only shorter trees to their left, right,
# up, or down.
def main():
    if len(sys.argv) < 2:
        print("Usage: advent-08-1.py <inputfile>")
        sys.exit(1)
    filename = sys.argv[1]

    with open(filename) as file:
        trees = list()
        num_cols = 0
        num_rows = 0
        for line in file:
            row = list(map(int, list(line.rstrip())))
            trees.append(row)
            num_cols = len(row)
            num_rows += 1
    trees = np.array(trees)
    # Trees on the outer rows and columns are always visible
    visible_trees = 2 * num_cols + 2 * num_rows - 4
    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            this_tree = trees[i, j]
            # Look left, right, up, down
            # are all trees in this direction shorter?
            if this_tree > max(trees[i, :j]) \
                    or this_tree > max(trees[i, j+1:]) \
                    or this_tree > max(trees[0:i, j]) \
                    or this_tree > max(trees[i+1:, j]):
                visible_trees += 1
    print(visible_trees)


if __name__ == '__main__':
    main()
