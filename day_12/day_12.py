import string
from collections import defaultdict


def get_possible_moves(coord: tuple, area: list, elevation_map: dict) -> list:
    possible_moves = []
    y, x = coord
    current_elevation = get_elevation(y, x, elevation_map, area)

    if len(area[0]) > (p := x - 1) >= 0 and get_elevation(y, p, elevation_map, area) <= current_elevation + 1:  # Left
        possible_moves.append((y, p))
    if len(area[0]) > (p := x + 1) >= 0 and get_elevation(y, p, elevation_map, area) <= current_elevation + 1:  # Right
        possible_moves.append((y, p))
    if len(area) > (p := y - 1) >= 0 and get_elevation(p, x, elevation_map, area) <= current_elevation + 1:  # Up
        possible_moves.append((p, x))
    if len(area) > (p := y + 1) >= 0 and get_elevation(p, x, elevation_map, area) <= current_elevation + 1:  # Down
        possible_moves.append((p, x))

    return possible_moves


def generate_graph_dict(area: list, elevation_map: dict) -> (defaultdict, list):
    graph = defaultdict(list)
    possible_start = []
    for y, y_val in enumerate(area):
        for x, x_val in enumerate(y_val):
            for possibility in get_possible_moves((y, x), area, elevation_map):
                graph[y, x].append(possibility)
            if x_val == 'a' or x_val == 'S':
                possible_start.append((y, x))
    return graph, possible_start


def get_elevation(y: int, x: int, elevation_map: dict, area: list) -> int:
    return elevation_map[area[y][x]]


def fetch_start_and_end_pos(area):
    curr_pos, end_pos = None, None
    for y, y_vals in enumerate(area):
        for x, x_vals in enumerate(y_vals):
            if x_vals == 'S':
                curr_pos = (y, x)
            elif x_vals == 'E':
                end_pos = (y, x)
    return curr_pos, end_pos


def get_depths_bfs(graph: defaultdict, start_pos: tuple, end_pos: tuple) -> int:
    depth = defaultdict(int)
    visited = defaultdict(bool)

    # Init:
    queue = [start_pos]
    depth[start_pos] = 0
    visited[start_pos] = True

    while queue:
        start_pos = queue.pop(0)

        for i in graph[start_pos]:
            if not visited[i]:
                queue.append(i)
                depth[i] = depth[start_pos] + 1
                visited[i] = True
                if i == end_pos:
                    return depth[i]

    return -1


def main():

    with open('input.txt') as f:
        area = [list(_) for _ in f.read().splitlines()]
    elevation_map = {val: height for height, val in enumerate(list(string.ascii_lowercase))}
    elevation_map['S'] = elevation_map['a']
    elevation_map['E'] = elevation_map['z']

    start_pos, end_pos = fetch_start_and_end_pos(area)
    directed_graph, possible_starting_points = generate_graph_dict(area, elevation_map)

    # Part 1
    print(get_depths_bfs(directed_graph, start_pos, end_pos))

    # Part 2
    steps = []
    for pos in possible_starting_points:
        steps.append(get_depths_bfs(directed_graph, pos, end_pos))

    print(min(filter(lambda x: x > 0, steps)))


if __name__ == '__main__':
    main()
