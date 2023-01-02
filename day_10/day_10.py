from itertools import cycle


def main():

    with open('input.txt') as f:
        instructions = [tuple(float(i) if i[-1].isdigit() else i for i in _.split(' ')) for _ in f.read().splitlines()]

    cycle_list = cycle(instructions)
    check_at_cycle, check_result = [20, 60, 100, 140, 180, 220], []
    x, addx, skip = 1.0, 0.0, False
    crt_dimensions, crt_plot = (40, 6), []
    lit, dark = '#', '.'

    for cycle_num, pixel_drawn in zip(
            range(1, crt_dimensions[0]*crt_dimensions[1]+1),
            cycle(list(range(crt_dimensions[0])))):

        sprite_pos = [x - 1, x, x + 1]
        if pixel_drawn in sprite_pos:
            crt_plot.append(lit)
        else:
            crt_plot.append(dark)

        if cycle_num in check_at_cycle:
            check_result.append(cycle_num * x)

        if skip:
            x += addx
            skip = False
        else:
            instruction = next(cycle_list)
            if instruction[0] == 'addx':
                addx, skip = instruction[1], True

    # Part 1
    print(sum(check_result))

    # Part 2
    for _ in range(0, len(crt_plot), 40): print(''.join(crt_plot[_:_+40]))


if __name__ == '__main__':
    main()
