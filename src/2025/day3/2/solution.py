import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    return lines


def find_largest_numbers(input: str) -> int:
    k = 12
    n = len(input)
    result = []
    start = 0

    for i in range(k):
        end = n - k + i + 1
        max_idx = start
        for j in range(start + 1, end):
            if input[j] > input[max_idx]:
                max_idx = j

        result.append(input[max_idx])
        start = max_idx + 1

    return int("".join(result))


lines = read_lines()
result = 0
for line in lines:
    line = line.decode("utf-8").strip()
    found = find_largest_numbers(line)
    result += found

print(result)
