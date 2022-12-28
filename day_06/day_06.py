def main():

    with open('input.txt') as f:
        datastream = [_ for _ in f.read().splitlines()]

    # Part 1
    for stream in datastream:
        for i in range(len(stream)):
            if len(set(stream[i:i+4])) == 4:
                print(i+4)
                break

    # Part 2
    for stream in datastream:
        for i in range(len(stream)):
            if len(set(stream[i:i+14])) == 14:
                print(i+14)
                break


if __name__ == '__main__':
    main()
