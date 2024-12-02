import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    lines = [line.decode("utf-8").strip() for line in lines]
    return lines


lines = read_lines()


def is_level_valid(level: list[str]):
    level_int = [int(l) for l in level]
    is_increasing = all(level_int[i] < level_int[i + 1] for i in range(len(level_int) - 1))
    is_decreasing = all(level_int[i] > level_int[i + 1] for i in range(len(level_int) - 1))

    if not (is_increasing or is_decreasing):
        return False

    for i in range(len(level_int) - 1):
        diff = abs(level_int[i] - level_int[i + 1])
        if diff < 1 or diff > 3:
            return False

    return True


report_count = 0
for line in lines:
    levels = line.split()
    if is_level_valid(levels):
        report_count += 1

print(report_count)
