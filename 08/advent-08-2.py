import numpy as np
import sys


# Given an array of tree heights, the scenic score is
# the product of the visibility ranges in all four directions
def main():
    if len(sys.argv) < 2:
        print("Usage: advent-08-2.py <inputfile>")
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

    max_scenic_score = 0
    # Scenic scores on the outer rows and columns are always 0
    # so we have to only loop over the inner trees
    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            scenic_score = score_left(trees, i, j) \
                           * score_right(trees, i, j) \
                           * score_up(trees, i, j)\
                           * score_down(trees, i, j)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    print(max_scenic_score)


def score_left(trees, i, j):
    score = 0
    for k in reversed(range(0, j)):
        score += 1
        if trees[i, j] <= trees[i, k]:
            return score
    return score


def score_right(trees, i, j):
    score = 0
    for k in range(j+1, trees.shape[1]):
        score += 1
        if trees[i, j] <= trees[i, k]:
            return score
    return score


def score_up(trees, i, j):
    score = 0
    for k in reversed(range(0, i)):
        score += 1
        if trees[i, j] <= trees[k, j]:
            return score
    return score


def score_down(trees, i, j):
    score = 0
    for k in range(i+1, trees.shape[0]):
        score += 1
        if trees[i, j] <= trees[k, j]:
            return score
    return score


if __name__ == '__main__':
    main()
