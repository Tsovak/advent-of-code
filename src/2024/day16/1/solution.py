import os


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


def calculate_distance_to_end(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve_maze(matrix: list[list[str]]) -> tuple[int, list[tuple[int, int, int]]]:
    start, end = find_start_end(matrix)

    # state: (r, c, direction, cost, path)
    initial_states = [
        (start[0], start[1], 0, 0, [(start[0], start[1], 0)]),  # start facing East
    ]

    best_score = float('inf')
    best_path = None

    visited = set()

    queue = initial_states

    while queue:
        # sort queue by total cost (with some heuristic guidance)
        queue.sort(key=lambda x: x[3] + calculate_distance_to_end((x[0], x[1]), end))

        r, c, dir_idx, total_cost, path = queue.pop(0)

        if (r, c) == end:
            if total_cost < best_score:
                best_score = total_cost
                best_path = path
            continue

        # avoid revisiting same state
        state_key = (r, c, dir_idx)
        if state_key in visited:
            continue
        visited.add(state_key)

        # try moving forward
        nr, nc = r + DIRECTIONS[dir_idx][0], c + DIRECTIONS[dir_idx][1]
        if (0 <= nr < len(matrix) and
                0 <= nc < len(matrix[0]) and
                matrix[nr][nc] != '#'):
            new_path = path + [(nr, nc, dir_idx)]
            queue.append((nr, nc, dir_idx, total_cost + 1, new_path))

        # try rotating clockwise
        cw_dir = (dir_idx + 1) % 4
        queue.append((r, c, cw_dir, total_cost + 1000, path + [(r, c, cw_dir)]))

        # try rotating counterclockwise
        ccw_dir = (dir_idx - 1 + 4) % 4
        queue.append((r, c, ccw_dir, total_cost + 1000, path + [(r, c, ccw_dir)]))

    return best_score, best_path


def visualize_path(matrix: list[list[str]], path: list[tuple[int, int, int]]) -> list[list[str]]:
    # create a copy of the matrix to modify
    visual_matrix = [row.copy() for row in matrix]

    # replace start and end with original characters
    start, end = find_start_end(matrix)
    visual_matrix[start[0]][start[1]] = 'S'
    visual_matrix[end[0]][end[1]] = 'E'

    # mark the path
    for (r, c, dir_idx) in path[1:]:  # Skip the first state
        if visual_matrix[r][c] in ['S', 'E', '#']:
            continue
        visual_matrix[r][c] = DIRECTION_CHARS[dir_idx]

    return visual_matrix


lines = read_input()
matrix = [list(line) for line in lines]
best_score, best_path = solve_maze(matrix)

path_matrix = visualize_path(matrix, best_path)

print(f"best path score: {best_score}")
print("\npath visualization:")
for row in path_matrix:
    print(''.join(row))
