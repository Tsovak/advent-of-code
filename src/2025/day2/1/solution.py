import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    return lines

def find_invalid_ranges(start:str, end:str) -> list[int] :
    start = int(start)
    end = int(end)
    if start >= end:
        return []

    total = []
    for i in range(start, end+1):
        s = str(i)
        half = len(s) // 2
        if s[:half] == s[half:]:
            total.append(i)

    return total

lines = read_lines()

line = lines[0].decode("utf-8")
ranges = line.split(",")
sums = 0
for r in ranges:
    start, end = r.split("-")
    sums += sum(find_invalid_ranges(start, end))

print(sums)