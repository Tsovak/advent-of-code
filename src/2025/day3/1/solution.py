import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    return lines


def find_largest_numbers(input: str) -> int:
    biggest = int(input[0])
    biggest_idx = 0
    for i in range(len(input) - 1):
        if int(input[i]) > biggest:
            biggest = int(input[i])
            biggest_idx = i

    next_biggest = int(input[biggest_idx + 1])
    for i in range(biggest_idx + 2, len(input)):
        if int(input[i]) > next_biggest:
            next_biggest = int(input[i])

    return biggest * 10 + next_biggest


lines = read_lines()
result = 0
for line in lines:
    line = line.decode("utf-8").strip()
    found = find_largest_numbers(line)
    result += found

print(result)