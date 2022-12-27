def main():

    shape_points = {
        'A': 1, # Rock A
        'B': 2, # Paper B
        'C': 3, # Scissor C
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    duel_points = {
             # LOOSE     DRAW      WIN
        'A': {'X': 'C', 'Y': 'A', 'Z': 'B'},
        'B': {'X': 'A', 'Y': 'B', 'Z': 'C'},
        'C': {'X': 'B', 'Y': 'C', 'Z': 'A'},
    }

    points = 0
    with open('input.txt') as f:
        for line in f.read().splitlines():
            opponent, outcome = line.split(' ')
            points += shape_points[outcome]
            points += shape_points[duel_points[opponent][outcome]]

    print(points)


if __name__ == '__main__':
    main()
