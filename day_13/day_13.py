import ast
from itertools import zip_longest


def is_right_order(left, right):

    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip_longest(left, right, fillvalue=-1):
            if l == -1:
                return True
            elif r == -1:
                return False

            if isinstance(l, list) or isinstance(r, list):
                is_right = is_right_order(l, r)
                if is_right is None:
                    continue
                else:
                    return is_right

            if l < r:
                return True
            elif l > r:
                return False
            else:
                continue

        return None

    if isinstance(left, int):
        return is_right_order([left], right)

    if isinstance(right, int):
        return is_right_order(left, [right])


def main():

    with open('input.txt') as f:
        file = f.read().splitlines()
        file_iter = iter(file)
        packet_pair = []
        for line in file_iter:
            packet_pair.append((ast.literal_eval(line), ast.literal_eval(next(file_iter))))
            next(file_iter, None)

    # Part 1
    is_right_list = []  # Left is smaller than right
    for idx, (left, right) in enumerate(packet_pair, 1):
        if is_right_order(left, right):
            is_right_list.append(idx)

    print(sum(is_right_list))

    # Part 2
    packet_pair.append(([[2]], [[6]]))
    packet_list = [_ for pair in packet_pair for _ in pair]  # flatten

    # Bubble sort implementation from the Internetz
    for iter_num in range(len(packet_list) - 1, 0, -1):
        for idx in range(iter_num):
            if not is_right_order(packet_list[idx], packet_list[idx + 1]):
                temp = packet_list[idx]
                packet_list[idx] = packet_list[idx + 1]
                packet_list[idx + 1] = temp

    product_of_divider_packets_indices = 1
    for i, _ in enumerate(packet_list, 1):
        if _ == [[2]] or _ == [[6]]:
            product_of_divider_packets_indices *= i

    print(product_of_divider_packets_indices)


if __name__ == '__main__':
    main()
