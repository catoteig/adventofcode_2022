from collections import defaultdict


def main():
    with open('input.txt') as f:
        grid = [[int(tree) for tree in line] for line in f.read().splitlines()]
        transposed_grid = [list(_) for _ in zip(*grid)]

    # Part 1
    visible_trees = set()

    # FROM WEST
    for y, row in enumerate(grid):
        tallest_tree = -1
        for x, tree in enumerate(row):
            if tree > tallest_tree:
                tallest_tree = tree
                visible_trees.add((x, y))

    # FROM EAST
    for y, row in enumerate(grid):
        tallest_tree = -1
        for x, tree in zip([_ for _ in reversed(range(len(row)))], list(reversed(row))):
            if tree > tallest_tree:
                tallest_tree = tree
                visible_trees.add((x, y))

    # NORTH
    for x, row in enumerate(transposed_grid):
        tallest_tree = -1
        for y, tree in enumerate(row):
            if tree > tallest_tree:
                tallest_tree = tree
                visible_trees.add((x, y))

    # SOUTH
    for x, row in enumerate(transposed_grid):
        tallest_tree = -1
        for y, tree in zip([_ for _ in reversed(range(len(row)))], list(reversed(row))):
            if tree > tallest_tree:
                tallest_tree = tree
                visible_trees.add((x, y))

    print(len(visible_trees))

    # Part 2
    scenic_scores = []

    for x, row in enumerate(grid):
        for i, tree_cabin in enumerate(row):
            dist_left, dist_right, dist_north, dist_south = 0, 0, 0, 0
            column = []
            for _ in range(len(row)):
                column.append(grid[_][i])

            # TO THE LEFT:
            for tree in reversed(row[0:i]):
                dist_left += 1
                if tree_cabin <= tree:
                    break

            # TO THE RIGHT:
            for tree in row[i+1:]:
                dist_right += 1
                if tree_cabin <= tree:
                    break

            # TO THE NORTH:
            for tree in reversed(column[0:x]):
                dist_north += 1
                if tree_cabin <= tree:
                    break

            # TO THE SOUTH:
            for tree in column[x+1:]:
                dist_south += 1
                if tree_cabin <= tree:
                    break

            scenic_scores.append(dist_right * dist_left * dist_north * dist_south)

    print(max(scenic_scores))


if __name__ == '__main__':
    main()
