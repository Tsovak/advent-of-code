import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    return lines


lines = read_lines()


def get_first_and_last_digit(line) -> tuple[int, int]:
    all_ints = [int(i) for i in line.decode("utf-8") if i.isdigit()]

    first = all_ints[0]
    last = all_ints[-1]

    return first, last


def get_all_numbers(lines: list[str]) -> list[int]:
    numbers = []

    for line in lines:
        first, last = get_first_and_last_digit(line)
        res = first * 10 + last
        numbers.append(res)

    return numbers


def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)


numbers = get_all_numbers(lines)
result = sum_numbers(numbers)
print(result)
