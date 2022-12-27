def main():

    calories = []
    with open('input.txt') as f:
        c = 0
        for _ in f.read().splitlines():
            if _ == '':
                calories.append(c)
                c = 0
            else:
                c += int(_)

    # Part 1
    print(max(calories))

    # Part 2
    calories.sort(reverse=True)
    print(sum(calories[0:3]))


if __name__ == '__main__':
    main()
