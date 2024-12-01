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


def hash(input):
    current = 0
    for c in input:
        current += ord(c)
        current *= 17
        current = current % 256
    return current


result = 0
for step in lines.split(","):
    result += hash(step)

print(result)