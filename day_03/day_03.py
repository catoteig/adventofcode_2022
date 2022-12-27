import string


def main():

    priority_list = list(string.ascii_lowercase)
    priority_list.extend(string.ascii_uppercase)

    # Part 1
    with open('input_test.txt') as f:
        items = [[line[:len(line)//2], line[len(line)//2:]] for line in f.read().splitlines()]

    sum_priority = 0
    for part1, part2 in items:
        intersect = (list(set(part1).intersection(part2)))
        sum_priority += priority_list.index(intersect[0]) + 1

    print(sum_priority)

    # Part 2
    with open('input.txt') as f:
        items = [line for line in f.read().splitlines()]

    sum_priority_2 = 0
    items_iterator = iter(items)
    for item in items_iterator:
        elf_1, elf_2, elf_3 = item, next(items_iterator), next(items_iterator)
        intersect = (list(set(elf_1).intersection(elf_2).intersection(elf_3)))
        sum_priority_2 += priority_list.index(intersect[0]) + 1

    print(sum_priority_2)


if __name__ == '__main__':
    main()
