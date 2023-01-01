def main():

    with open('input.txt') as f:
        motions = [tuple(int(i) if i.isdigit() else i for i in _.split(' ')) for _ in f.read().splitlines()]

    tail_log = set()
    head_x, head_y, tail_x, tail_y = 0, 0, 0, 0

    for direction, steps in motions:
        for step in range(steps):
            # Head:
            if direction == 'R': head_x += 1
            if direction == 'L': head_x -= 1
            if direction == 'U': head_y += 1
            if direction == 'D': head_y -= 1

            # Tail:
            if (tail_x, tail_y) == (head_x, head_y):  # Head and tail on same spot
                pass
            elif abs(tail_x - head_x) <= 1 and abs(tail_y - head_y) <= 1:  # Head and tail touching
                pass
            elif tail_x == head_x and abs(tail_y - head_y) > 1:  # Vertical move
                tail_y += 1 if direction == 'U' else -1
            elif tail_y == head_y and abs(tail_x - head_x) > 1:  # Horizontal move
                tail_x += 1 if direction == 'R' else -1
            elif abs(head_x - tail_x) >= 2 and abs(head_y - tail_y) >= 1:  # Diagonal horizontal move
                tail_x += 1 if direction == 'R' else -1
                tail_y = head_y
            elif abs(head_x - tail_x) >= 1 and abs(head_y - tail_y) >= 2:  # Diagonal vertical move
                tail_y += 1 if direction == 'U' else -1
                tail_x = head_x
            tail_log.add((tail_x, tail_y))

    print(len(tail_log))


if __name__ == '__main__':
    main()
