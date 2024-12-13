import os
from collections import namedtuple

import numpy as np


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


Point = namedtuple('Point', ['X', 'Y'])


def get_coefficients(button_a: Point, button_b: Point, prize: Point) -> tuple:
    arr = np.array([
        [button_a.X, button_b.X],
        [button_a.Y, button_b.Y]
    ])

    b = np.array([prize.X, prize.Y])
    x, y = np.linalg.solve(arr, b)
    return round(x), round(y)


def get_tokens(lines: list[str]):
    groups = [lines[i:i + 3] for i in range(0, len(lines), 4)]

    tokens = 0
    for group in groups:
        points = []
        for line in group:
            x_val = int(''.join(filter(str.isdigit, line.split(',')[0])))
            y_val = int(''.join(filter(str.isdigit, line.split(',')[1])))
            points.append(Point(x_val, y_val))

        button_a, button_b, prize = points
        presses_a, presses_b = get_coefficients(button_a, button_b, prize)
        if (
                presses_a * button_a.X + presses_b * button_b.X == prize.X and
                presses_a * button_a.Y + presses_b * button_b.Y == prize.Y
        ):
            tokens += presses_a * 3 + presses_b

    return tokens


lines = read_lines()
result = get_tokens(lines)
print(result)
