import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    return lines


lines = read_lines()

first_column = []
second_column = []

for line in lines:
    line = line.decode("utf-8")
    first, second = line.split()
    first_column.append(int(first))
    second_column.append(int(second))

first_column.sort()
second_column.sort()

result = sum(abs(a - b) for a, b in zip(sorted(first_column), sorted(second_column)))
print(result)
# 1341714
