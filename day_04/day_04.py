def main():

    with open('input.txt') as f:
        assigment_pairs = [[[int(elf) for elf in pair.split('-')] for pair in line.split(',')] for line in f.read().splitlines()]

    total = 0
    for elf_1, elf_2 in assigment_pairs:
        id_1 = [_ for _ in range(elf_1[0], elf_1[1]+1)]
        id_2 = [_ for _ in range(elf_2[0], elf_2[1]+1)]

        if all(item in id_1 for item in id_2) or all(item in id_2 for item in id_1):
            total += 1

    print(total)


if __name__ == '__main__':
    main()
