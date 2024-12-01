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

maps = []
sums = 0

def detect_smudge(left, right):
    diffs = []
    for index, (l, r) in enumerate(zip(left, right[::-1])):
        if l != r:
            diffs.append(index)
    return diffs


def detect_reflections(map, multiplier):
    global sums

    for x in range(1, len(map[0])):
        lefts = []
        rights = []
        for line in map:
            left = line[:x]
            right = line[x:]
            length_diff = len(left) - len(right)
            if length_diff < 0:
                right = right[:length_diff]
            elif length_diff > 0:
                left = left[length_diff:]

            lefts.append(left)
            rights.append(right)

        left = "".join(lefts[::-1])
        right = "".join(rights)

        smudges = detect_smudge(left, right)
        if len(smudges) == 1:
            smudge_index = smudges[0]
            new_sign = "."
            if left[smudge_index] == ".":
                new_sign = "#"
            temp = [c for c in left]
            temp[smudge_index] = new_sign
            left = "".join(temp)

            if left == right[::-1]:
                sums += x * multiplier

lines = "".join(lines)
for patterns in lines.split("\n\n"):
    map = patterns.split()
    maps.append(map)

for map in maps:
    detect_reflections(map, 1)

    # rotate map
    map = list(zip(*map))
    map = ["".join(m) for m in map]
    map = [l for l in map[::-1]]
    detect_reflections(map, 100)

print(f"Result: {sums}")
