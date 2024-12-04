import os

import numpy as np

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


def find_xs_count(line: str) -> int:
    return line.count("XMAS") + line.count("SAMX")


lines = read_lines()
arr = np.array([list(line) for line in lines])

diags = [arr[::-1, :].diagonal(i) for i in range(-arr.shape[0] + 1, arr.shape[1])]
diag2 = [arr.diagonal(i) for i in range(arr.shape[1] - 1, -arr.shape[0], -1)]
diags.extend(diag2)

rows = [list(row) for row in arr]
columns = [list(column) for column in arr.T]

# reversed_rows = [list(row[::-1]) for row in arr]
# reversed_columns = [list(column[::-1]) for column in arr.T]
# reversed_diag = [list(d[::-1]) for d in diags]

full_array = diags + rows + columns
full_string_arr = ["".join(v) for v in full_array]

count = sum(find_xs_count(line) for line in full_string_arr)
print(count)
