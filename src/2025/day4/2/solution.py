import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    return lines


def count_rolls(matrix):
    row_len, col_len = len(matrix), len(matrix[0])

    def capture_squares_around(x, y):
        x_start, x_end = x - 1, x + 1
        x_start = 0 if x_start < 0 else x_start
        x_end = row_len - 1 if x_end >= row_len else x_end

        y_start, y_end = y - 1, y + 1
        y_start = 0 if y_start < 0 else y_start
        y_end = col_len - 1 if y_end >= col_len else y_end

        submatrix = [row[y_start : y_end + 1] for row in matrix[x_start : x_end + 1]]
        return submatrix


    guard = [
        (i, j)
        for i in range(row_len)
        for j in range(col_len)
        if matrix[i][j] == "@"
    ]

    removed = True
    total = 0
    while removed:
        removed = False
        remember = []
        for g in guard:
            submatrix = capture_squares_around(*g)
            flat = [cell for row in submatrix for cell in row]
            count = flat.count("@")
            if count < 5:
                matrix[g[0]][g[1]] = "x"
                remember.append(g)
                total += 1
                removed = True

        for g in remember:
            guard.remove(g)

    return total


lines = read_lines()
matrix = [list(line.decode("utf-8").strip()) for line in lines]

result = count_rolls(matrix)
print(result)