import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.read().splitlines()

    return lines

def print_matrix(matrix: list[list[str]]) -> None:
    for row in matrix:
        print("".join(row))
    print()


def count_timelines(lines: list[str]) -> int:
    s = [
        (i, j)
        for i in range(len(matrix))
        for j in range(len(matrix[0]))
        if matrix[i][j] == "S"
    ]

    _, start_col = s[0]
    paths = {start_col: 1}

    for row in lines[1:]:
        new_paths = {}
        for col, count in paths.items():
            if col < 0 or col >= len(row):
                continue
            if row[col] == "^":
                new_paths[col - 1] = new_paths.get(col - 1, 0) + count
                new_paths[col + 1] = new_paths.get(col + 1, 0) + count
            else:
                new_paths[col] = new_paths.get(col, 0) + count
        paths = new_paths

    return sum(paths.values())

lines = read_lines()

matrix = []
for line in lines:
    line = line.decode("utf-8")
    parts = [l for l in line]
    matrix.append(parts)

print(count_timelines(matrix))