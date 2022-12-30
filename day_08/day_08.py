def main():

    with open('input.txt') as f:
        grid = [[int(tree) for tree in line] for line in f.read().splitlines()]
        transposed_grid = [list(_) for _ in zip(*grid)]

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


if __name__ == '__main__':
    main()
