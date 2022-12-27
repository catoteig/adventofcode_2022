import string


def main():

    priority_list = list(string.ascii_lowercase)
    priority_list.extend(string.ascii_uppercase)

    with open('input.txt') as f:
        items = [[line[:len(line)//2], line[len(line)//2:]] for line in f.read().splitlines()]

    sum_priority = 0
    for part1, part2 in items:
        intersect = (list(set(part1).intersection(part2)))
        sum_priority += priority_list.index(intersect[0]) + 1

    print(sum_priority)


if __name__ == '__main__':
    main()
