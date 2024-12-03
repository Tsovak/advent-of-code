import os
import re

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    lines = [line.decode("utf-8").strip() for line in lines]
    return lines


lines = read_lines()
lines_joined = "".join(lines)

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))")

matches = pattern.findall(lines_joined)
result = 0
do = True

for a, b, doIt, dontDoIt in matches:
    if doIt or dontDoIt:
        do = bool(doIt)
    else:
        res = int(a) * int(b)
        result += res * do

print(result)
