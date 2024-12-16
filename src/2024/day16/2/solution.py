import os
from collections import defaultdict


def read_input() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


# clockwise order: East, North, West, South
DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]
DIRECTION_CHARS = ['>', '^', '<', 'v']


def find_start_end(matrix: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    start, end = None, None
    for r, row in enumerate(matrix):
        for c, cell in enumerate(row):
            if cell == 'S':
                start = (r, c)
            elif cell == 'E':
                end = (r, c)
    return start, end


def solve_maze(matrix: list[list[str]]) -> tuple[int, set[tuple[int, int]]]:
    start, end = find_start_end(matrix)

    min_costs = {}
    best_paths = []
    best_cost = float('inf')

    # state: (r, c, direction, cost, path)
    queue = [(start[0], start[1], 0, 0, [(start[0], start[1])])]

    while queue:
        r, c, dir_idx, cost, path = queue.pop(0)

        if cost > best_cost:
            continue

        state = (r, c, dir_idx)
        if state in min_costs and min_costs[state] < cost:
            continue
        min_costs[state] = cost

        if (r, c) == end:
            if cost < best_cost:
                best_cost = cost
                best_paths = [path]
            elif cost == best_cost:
                best_paths.append(path)
            continue

        # move forward
        nr, nc = r + DIRECTIONS[dir_idx][0], c + DIRECTIONS[dir_idx][1]
        if (0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] != '#'):
            queue.append((nr, nc, dir_idx, cost + 1, path + [(nr, nc)]))

        # rotate clockwise and counterclockwise
        for new_dir in [(dir_idx + 1) % 4, (dir_idx - 1) % 4]:
            queue.append((r, c, new_dir, cost + 1000, path))

    # collect all tiles from best paths
    best_tiles = set()
    for path in best_paths:
        for pos in path:
            best_tiles.add(pos)

    return best_cost, best_tiles


def solve_maze(matrix: list[list[str]]) -> set[tuple[int, int]]:
    start, end = find_start_end(matrix)
    min_costs = defaultdict(lambda: float('inf'))  # (r, c, dir) -> cost
    best_tiles = set()
    best_total_cost = float('inf')

    # queue: (r, c, direction, cost, path)
    queue = [(start[0], start[1], 0, 0, [(start[0], start[1])])]

    while queue:
        r, c, dir_idx, cost, path = queue.pop(0)

        # skip paths that exceed best cost
        if cost > best_total_cost:
            continue

        if (r, c) == end:
            if cost <= best_total_cost:
                if cost < best_total_cost:
                    best_total_cost = cost
                    best_tiles.clear()
                # add all positions in this path
                best_tiles.update((r, c) for r, c in path)
            continue

        state = (r, c, dir_idx)
        # only prune if we found strictly better path to this state
        if cost > min_costs[state]:
            continue
        min_costs[state] = cost

        # forward move
        nr, nc = r + DIRECTIONS[dir_idx][0], c + DIRECTIONS[dir_idx][1]
        if (0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] != '#'):
            queue.append((nr, nc, dir_idx, cost + 1, path + [(nr, nc)]))

        # rotations
        for new_dir in [(dir_idx + 1) % 4, (dir_idx - 1) % 4]:
            queue.append((r, c, new_dir, cost + 1000, path))

    return best_tiles


lines = read_input()
matrix = [list(line) for line in lines]
best_tiles = solve_maze(matrix)

print(f"result: {len(best_tiles)}")
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == '#':
            print('#', end='')
        elif (r, c) in best_tiles:
            print('O', end='')
        else:
            print('.', end='')
    print()
