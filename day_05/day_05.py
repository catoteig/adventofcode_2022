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


def main():

    moves, stacks = parse_txt('input.txt')

    for n, stack_from, stack_to in moves:
        stacks[stack_from], stacks[stack_to] = move_crates(n, stacks[stack_from], stacks[stack_to])

    print(''.join([str(stacks[stack][-1]) for stack in stacks]))


if __name__ == '__main__':
    main()
