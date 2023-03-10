import copy
from collections import defaultdict


def parse_txt(filename):
    moves, stacks_unparsed = [], []
    with open(filename) as f:
        for line in f.read().splitlines():
            if line[0:4] == 'move':
                split = line.split(' ')
                moves.append([int(split[_]) for _ in range(1, len(split), 2)])
            elif line != '':
                stacks_unparsed.append(line)

    stacks = defaultdict(list)
    stacks_unparsed.pop()  # remove idx row

    for stack in reversed(stacks_unparsed):
        for i, _ in enumerate(range(1, len(stack), 4)):
            if str.isalnum(stack[_]):
                stacks[i+1].append(stack[_])

    return moves, stacks


def move_crates(n, stack_from, stack_to):
    for move in range(n):
        stack_to.append(stack_from.pop())
    return stack_from, stack_to


def move_crates_CrateMover9001(n, stack_from, stack_to):
    temp = []
    for move in range(n):
        temp.append(stack_from.pop())
    stack_to.extend(reversed(temp))
    return stack_from, stack_to


def main():

    moves, stacks = parse_txt('input.txt')
    stacks_part2 = copy.deepcopy(stacks)

    # Part 1
    for n, stack_from, stack_to in moves:
        stacks[stack_from], stacks[stack_to] = move_crates(n, stacks[stack_from], stacks[stack_to])

    print(''.join([str(stacks[stack][-1]) for stack in stacks]))

    # Part 2
    for n, stack_from, stack_to in moves:
        stacks_part2[stack_from], stacks_part2[stack_to] = move_crates_CrateMover9001(n, stacks_part2[stack_from], stacks_part2[stack_to])

    print(''.join([str(stacks_part2[stack][-1]) for stack in stacks_part2]))


if __name__ == '__main__':
    main()
