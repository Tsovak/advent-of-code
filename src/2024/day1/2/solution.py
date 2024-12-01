import os
from collections import Counter

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


# sort columns in acsending order
first_column.sort()
second_column.sort()

right_counter = Counter(second_column)

similarity_score = sum(num * right_counter[num] for num in first_column)
print(similarity_score) # 27384707
