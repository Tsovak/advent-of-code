import math
import itertools as it
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    # convert bytes to string
    lines = [line.decode("utf-8") for line in lines]
    return lines


lines = read_lines()


def closed_range(start, stop, step=1):
    dir = 1 if (step > 0) else -1
    return range(start, stop + dir, step)


def get_number(i, j) -> int:
    start_x, start_y = i - 1, j - 1
    end_x, end_y = i + 1, j + 1

    if i == 0:
        start_x = 0
    if j == 0:
        start_y = 0

    if i == len(lines) - 1:
        end_x = len(lines) - 1
    if j + 1 == len(lines[0]) - 1:
        end_y = j + 1

    num = []
    for x in closed_range(start_x, end_x):
        y = start_y
        while y <= end_y and lines[x][y] != "\n":

            start = y
            while start > 0 and lines[x][start].isdigit() and lines[x][start - 1].isdigit():
                start -= 1

            if start < 0:
                start = 0
            k = start
            while k < len(lines[x]) and lines[x][k].isdigit():
                k += 1

            if start < k:
                # was found

                if lines[x][start:k] == "":
                    y += start
                    continue

                number = int(lines[x][start:k])
                num.append(number)
                y = k
                continue

            end = y
            while end < len(lines[x]) and lines[x][end].isdigit():
                end += 1
            if end > y:
                # was found
                number = int(lines[x][y:end])
                num.append(number)
                y = end
                continue
            y += 1

    if len(num) != 2:
        return 0

    print("num=", num)
    result = 1
    for n in num:
        result *= n
    return result


def get_numbers() -> []:
    numbers = []
    for i, line in enumerate(lines):
        j = 0
        while j < len(line):
            char = line[j]
            if char == "*":
                num = get_number(i, j)
                numbers.append(num)
            j += 1

    return numbers


num = get_numbers()
print(num)
total = sum_numbers(num)
print(total)
