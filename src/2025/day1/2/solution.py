import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    return lines

lines = read_lines()

starting_position = 50
total = 0

def rotate(current: int, isLeft, distance: int) -> int:
    global total

    if isLeft:
        return (current - distance) % 100
    else:
        return (current + distance) % 100

def count_zeros(current: int, isLeft: bool, distance: int) -> int:
    if isLeft:
        k_min = 100 if current == 0 else current
    else:
        k_min = 100 if current == 0 else (100 - current)

    if distance >= k_min:
        return (distance - k_min) // 100 + 1
    else:
        return 0



for line in lines:
    line = line.decode("utf-8")
    isLeft, value = line[0]=="L", int(line[1:])
    zeroes = count_zeros(starting_position, isLeft, value)
    total += zeroes
    starting_position = rotate(starting_position, isLeft, value)

print(total)

