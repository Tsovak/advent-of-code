import os


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


lines = read_lines()
matrix_str = [list(line) for line in lines]
matrix = [[int(cell) for cell in row] for row in matrix_str]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def find_unique_path(grid):
    def dfs(x, y, current_num, path, visited):
        # check bounds and validity
        if (
                not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or
                grid[x][y] != current_num or
                (x, y) in visited
        ):
            return []

        if current_num == 9:
            return [path + [(x, y)]]

        new_visited = visited.copy()
        new_visited.add((x, y))

        valid_paths = []
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            next_num = current_num + 1

            sub_paths = dfs(new_x, new_y, next_num, path + [(x, y)], new_visited)
            valid_paths.extend(sub_paths)

        return valid_paths

    unique_paths = set()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                paths = dfs(x, y, 0, [], set())
                for path in paths:
                    unique_paths.add(tuple(path))

    return [list(path) for path in unique_paths]


paths = find_unique_path(matrix)
print(len(paths))
