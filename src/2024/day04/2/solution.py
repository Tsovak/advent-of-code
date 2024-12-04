import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


def find_xs_count(m: list[list[str]]) -> int:
    corners = (m[0][0], m[0][2], m[2][0], m[2][2])
    center = m[1][1]

    valid_patterns = [
        ("M", "S", "M", "S"),
        ("S", "M", "S", "M"),
        ("S", "S", "M", "M"),
        ("M", "M", "S", "S"),
    ]

    return center == "A" and corners in valid_patterns


def get_3x3_submatrices(matrix):
    if not matrix or len(matrix) < 3 or len(matrix[0]) < 3:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    submatrices = []

    for i in range(rows - 2):
        for j in range(cols - 2):
            submatrix = [matrix[i][j : j + 3], matrix[i + 1][j : j + 3], matrix[i + 2][j : j + 3]]
            submatrices.append(submatrix)

    return submatrices


lines = read_lines()
arr = [list(line) for line in lines]

submatrices = get_3x3_submatrices(arr)
count = sum(find_xs_count(submatrix) for submatrix in submatrices)
print(count)
