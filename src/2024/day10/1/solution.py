import os


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


lines = read_lines()
matrix_str = [list(line) for line in lines]
matrix = [[int(cell) for cell in row] for row in matrix_str]


def calculate_trailhead_scores(grid):
    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def find_paths(start_x, start_y):
        def dfs(x, y, current_height, path, visited):
            if not is_valid(x, y) or grid[x][y] != current_height or (x, y) in visited:
                return set()

            new_visited = visited.copy()
            new_visited.add((x, y))

            if current_height == 9:
                return {tuple(path + [(x, y)])}

            paths = set()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                sub_paths = dfs(new_x, new_y, current_height + 1, path + [(x, y)], new_visited)
                paths.update(sub_paths)

            return paths

        all_paths = dfs(start_x, start_y, 0, [], set())
        return all_paths

    def count_reachable_nines(paths):
        nines = set((x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 9)
        return len(set(path[-1] for path in paths if path[-1] in nines))

    starting_positions = [
        (i, j)
        for i in range(len(matrix[0]))
        for j in range(len(matrix))
        if matrix[i][j] == 0
    ]

    scores = []
    for start_x, start_y in starting_positions:
        paths = find_paths(start_x, start_y)
        scores.append(count_reachable_nines(paths))

    return scores


scores = calculate_trailhead_scores(matrix)
print(sum(scores))
