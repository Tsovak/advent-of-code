import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    return lines

lines = read_lines()

starting_position = 50

def rotate(current: int, isLeft, distance: int) -> int:
    if isLeft:
        return (current - distance) % 100
    else:
        return (current + distance) % 100


total = 0
for line in lines:
    line = line.decode("utf-8")
    isLeft, value = line[0]=="L", int(line[1:])
    starting_position = rotate(starting_position, isLeft, value)
    print(line[0], value, "=", starting_position)
    if starting_position == 0:
        total += 1

print(total)

