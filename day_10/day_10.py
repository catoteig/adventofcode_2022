from itertools import cycle


def main():

    with open('input.txt') as f:
        instructions = [tuple(float(i) if i[-1].isdigit() else i for i in _.split(' ')) for _ in f.read().splitlines()]

    cycle_list = cycle(instructions)
    check_at_cycle, check_result = [20, 60, 100, 140, 180, 220], []
    x, addx, skip = 1.0, 0.0, False

    for cycle_num in range(1, check_at_cycle[-1]+1):
        if cycle_num in check_at_cycle:
            check_result.append(cycle_num * x)

        if skip:
            x += addx
            skip = False
        else:
            instruction = next(cycle_list)
            if instruction[0] == 'addx':
                addx, skip = instruction[1], True

    print(sum(check_result))


if __name__ == '__main__':
    main()
