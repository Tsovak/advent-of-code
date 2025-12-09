import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.read().splitlines()

    return lines


def calculate_rectangle_square(p1, p2):
    width = abs(p2[0] - p1[0]) + 1
    height = abs(p2[1] - p1[1]) + 1
    return width * height


lines = read_lines()

dataset = set()
for line in lines:
    line = line.decode("utf-8")
    y, x = map(int, line.split(","))
    dataset.add((x, y))

maximum_rec = -1
points = list(dataset)
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        c = calculate_rectangle_square(points[i], points[j])
        if c > maximum_rec:
            maximum_rec = c

print(maximum_rec)
