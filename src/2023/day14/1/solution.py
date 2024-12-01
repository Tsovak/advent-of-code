import re
import os
from itertools import combinations

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    # convert bytes to string
    lines = [line.decode("utf-8") for line in lines]
    return lines


def read_file_into_matrix():
    with open(os.path.join(ROOT_DIR, 'data.txt'), "r") as file:
        return [list(line.strip()) for line in file]


lines = read_lines()
lines = "".join(lines)

input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

# with open("input.txt") as f:
#    input = f.read()

data = []


def get_lowest_free_field(x, y):
    result = y
    for check_y in range(y, -1, -1):
        if check_y == y:
            continue
        if data[check_y][x] == ".":
            result = check_y
        else:
            break
    return result


for line in lines.splitlines():
    data_line = [c for c in line]
    data.append(data_line)

for x in range(len(data[0])):
    for y in range(len(data)):
        if data[y][x] == "O":
            lowest_free_y = get_lowest_free_field(x, y)
            if lowest_free_y != y:
                data[lowest_free_y][x] = "O"
                data[y][x] = "."

sums = 0

data = data[::-1]
for y in range(len(data)):
    line = data[y]
    num = line.count("O")
    sums += num * (y + 1)

print(f"Result: {sums}")