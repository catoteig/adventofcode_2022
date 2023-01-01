def main():

    with open('input.txt') as f:
        motions = [tuple(int(i) if i.isdigit() else i for i in _.split(' ')) for _ in f.read().splitlines()]

    tail_length = 9  # <--- Part 1: Length = 1 ; Part 2: Length = 9
    tail = [(0, 0)] * tail_length
    tail_end_log = set()
    head_x, head_y = 0, 0

    for direction, steps in motions:
        for step in range(steps):
            # Head:
            if direction == 'R': head_x += 1
            if direction == 'L': head_x -= 1
            if direction == 'U': head_y += 1
            if direction == 'D': head_y -= 1

            temp_head_x, temp_head_y = head_x, head_y

            for idx, (tail_x, tail_y) in enumerate(tail):
                if (tail_x, tail_y) == (temp_head_x, temp_head_y):  # Head and tail on same spot
                    pass
                elif abs(tail_x - temp_head_x) <= 1 and abs(tail_y - temp_head_y) <= 1:  # Head and tail touching
                    pass
                elif tail_x == temp_head_x and abs(tail_y - temp_head_y) > 1:  # Vertical move
                    tail_y += 1 if (temp_head_y > tail_y) else -1
                elif tail_y == temp_head_y and abs(tail_x - temp_head_x) > 1:  # Horizontal move
                    tail_x += 1 if (temp_head_x > tail_x) else -1
                elif abs(temp_head_x - tail_x) >= 1 and abs(temp_head_y - tail_y) >= 1:  # Diagonal move
                    if temp_head_y > tail_y:
                        tail_y += 1
                    elif temp_head_y < tail_y:
                        tail_y -= 1

                    if temp_head_x > tail_x:
                        tail_x += 1
                    elif temp_head_x < tail_x:
                        tail_x -= 1

                temp_head_x, temp_head_y = tail_x, tail_y
                tail[idx] = (tail_x, tail_y)

                if idx == len(tail)-1:
                    tail_end_log.add((tail_x, tail_y))

    print(len(tail_end_log))


if __name__ == '__main__':
    main()
