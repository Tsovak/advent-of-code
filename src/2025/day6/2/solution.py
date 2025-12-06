import os
from typing import Generator

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.read().splitlines()

    return lines

def normalize(matrix: list[list[str]]) -> Generator[tuple[list[int], str], None, None]:
    rows = len(matrix)
    cols = len(matrix[0])

    numbers = []
    operation = None

    for col_idx in range(cols - 1, -1, -1):
        column = [matrix[row][col_idx] for row in range(rows)]

        if all(c == " " for c in column):
            if numbers:
                yield numbers, operation
                numbers = []
                operation = None
            continue

        bottom = column[-1]
        if bottom in ["+", "*"]:
            operation = bottom
            column = column[:-1]

        digits = "".join(c for c in column if c.isdigit())
        if digits:
            numbers.append(int(digits))

    if numbers:
        yield numbers, operation



lines = read_lines()

matrix = []
for line in lines:
    line = line.decode("utf-8")
    parts = [l for l in line]
    matrix.append(parts)


total = 0
for col, operation in normalize(matrix):
    match operation:
        case "+":
            summed = sum(x for x in col)
            total += summed
            print(col, ": ", summed)
        case "*":
            mltp = 1
            for x in col:
                mltp *= x
            total += mltp
            print(col, ": ", mltp)

print(total)