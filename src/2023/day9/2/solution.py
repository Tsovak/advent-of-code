import re
import os
from itertools import pairwise

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    # convert bytes to string
    lines = [line.decode("utf-8") for line in lines]
    return lines


lines = read_lines()

values = []
for line in lines:
    line_values = [int(x) for x in line.split()]
    values.append(line_values)

histories = 0

for line_values in values:
    extrapolation_data = []
    extrapolation_data.append(line_values)

    while True:
        diffs = [y - x for (x, y) in pairwise(extrapolation_data[-1])]
        extrapolation_data.append(diffs)

        if all(d == 0 for d in diffs):
            break

    last_history = extrapolation_data[-1][0]
    for extrapolations in extrapolation_data[::-1][1:]:
        last_history = extrapolations[0] - last_history

    histories += last_history

print(f"Sum of histories: {histories}")