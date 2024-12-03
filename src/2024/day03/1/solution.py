import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    lines = [line.decode("utf-8").strip() for line in lines]
    return lines


lines = read_lines()

import re

pattern = 'mul\((\d{1,3}),(\d{1,3})\)'


def extract(line: str):
    matches = re.findall(pattern, line)
    numbers = [(int(n1) * int(n2)) for n1, n2 in matches]
    return sum(numbers)


result = sum([
    extract(line)
    for line in lines
])

print(result)  # 163931492
