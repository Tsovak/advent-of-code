import os
from itertools import product


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


lines = read_lines()
matrix = [list(line) for line in lines]


def is_within_bounds(point, bounds):
    return 0 <= point[0] < bounds[0] and 0 <= point[1] < bounds[1]


def find_antinodes(matrix):
    height, width = len(matrix), len(matrix[0])
    antennas = {}

    # antennas by frequency
    for y, x in product(range(height), range(width)):
        if matrix[y][x] != '.':
            antennas.setdefault(matrix[y][x], []).append((x, y))

    antinodes = set()

    for _, antenna_list in antennas.items():
        for i, (x1, y1) in enumerate(antenna_list):
            for (x2, y2) in antenna_list[i + 1:]:
                x_diff, y_diff = x2 - x1, y2 - y1

                # calculate symmetrical antinodes
                outside_a = (x1 - x_diff, y1 - y_diff)
                outside_b = (x2 + x_diff, y2 + y_diff)

                if is_within_bounds(outside_a, (width, height)):
                    antinodes.add(outside_a)
                if is_within_bounds(outside_b, (width, height)):
                    antinodes.add(outside_b)

    return len(antinodes)


result = find_antinodes(matrix)
print(result)
