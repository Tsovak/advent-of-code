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


def is_valid(i, j, num_length) -> bool:
    start_x, start_y = i - 1, j - 1
    end_x, end_y = i + 1, j + num_length

    if i == 0:
        start_x = 0
    if j == 0:
        start_y = 0

    if i == len(lines) - 1:
        end_x = len(lines) - 1
    if j + num_length == len(lines[0]) - 1:
        end_y = j + num_length

    l = ""
    for x in closed_range(start_x, end_x):
        l = l + "\n"
        for y in closed_range(start_y, end_y):
            l = l + lines[x][y]
            if lines[x][y] != "." and not lines[x][y].isdigit() and lines[x][y] != "\n":
                print(l)
                return True

    print(l)
    return False


def get_numbers() -> []:
    numbers = []
    for i, line in enumerate(lines):
        decoded = line
        start = 0
        while start < len(line):
            j = start
            char = line[j]
            if char.isdigit():
                k = j
                while k < len(decoded) and decoded[k].isdigit():
                    k += 1
                number = int(decoded[j:k])
                if number == 202:
                    print("here")
                if is_valid(i, j, len(str(number))):
                    numbers.append(number)
                start = k
                continue
            start += 1

    return numbers


num = get_numbers()
sum = sum_numbers(num)
print(sum)
