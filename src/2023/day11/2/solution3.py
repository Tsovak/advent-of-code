import re
import os
from itertools import combinations

import numpy as np
from tqdm import tqdm

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

XXX = 1000000

filename = os.path.join(ROOT_DIR, 'data.txt')
def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    # convert bytes to string
    lines = [line.decode("utf-8").strip() for line in lines]
    return lines


def read_file_into_matrix():
    with open(os.path.join(ROOT_DIR, 'data.txt'), "r") as file:
        return [line.strip() for line in file]


with open(filename, "r") as f:
    m = [list(line.strip()) for line in f]

    w, h = len(m[0]), len(m)

    galaxies = [(x, y) for y in range(h) for x in range(w) if m[y][x] == "#"]
    cols = [x for x in range(w) if all(m[y][x] == "." for y in range(h))]
    rows = [y for y in range(h) if all(m[y][x] == "." for x in range(w))]


    def expand(factor):
        expanded = []

        for (x, y) in galaxies:
            cs = (factor - 1) * sum(1 for c in cols if c < x)
            rs = (factor - 1) * sum(1 for r in rows if r < y)

            expanded.append((x + cs, y + rs))

        return expanded


    def manhattan(p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        return abs(x2 - x1) + abs(y2 - y1)


    part1 = sum(manhattan(g1, g2) for g1, g2 in combinations(expand(2), 2))
    part2 = sum(manhattan(g1, g2) for g1, g2 in combinations(expand(1000000), 2))

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")