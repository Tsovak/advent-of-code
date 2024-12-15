import os


def read_input() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


def parse() -> tuple[
    list[list[str]],
    list[tuple[int, int]],
    tuple[int, int]
]:
    lines = read_input()
    matrix = [list(line) for line in lines if "<" not in line][:-1]
    robot_position = [(i, j) for i, line in enumerate(matrix) for j, c in enumerate(line) if c == "@"][0]
    directions_commands = lines[len(matrix) + 1:]
    directions_commands = "".join(directions_commands)

    directions: list[tuple[int, int]] = []

    for k, v in enumerate(directions_commands):
        if v == '<':
            directions.append((0, -1))
        elif v == '>':
            directions.append((0, 1))
        elif v == '^':
            directions.append((-1, 0))
        elif v == 'v':
            directions.append((1, 0))

    return matrix, directions, robot_position


def can_push_boxes(matrix: list[list[str]], start_x: int, start_y: int, dx: int, dy: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    x, y = start_x, start_y

    while 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 'O':
        x += dx
        y += dy

    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == '.'


def push_boxes(matrix: list[list[str]], start_x: int, start_y: int, dx: int, dy: int):
    rows, cols = len(matrix), len(matrix[0])
    x, y = start_x, start_y

    boxes = []
    while 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 'O':
        boxes.append((x, y))
        x += dx
        y += dy

    for (box_x, box_y) in reversed(boxes):
        matrix[box_x + dx][box_y + dy] = 'O'
        matrix[box_x][box_y] = '.'


def move_robot(
        matrix: list[list[str]],
        directions: list[tuple[int, int]],
        robot_position: tuple[int, int]
) -> list[list[str]]:
    rows, cols = len(matrix), len(matrix[0])
    x, y = robot_position
    matrix[x][y] = '.'  # remove robot from initial position

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        # check if the next cell is within bounds
        if 0 <= new_x < rows and 0 <= new_y < cols:
            # if the next cell is empty, move robot
            if matrix[new_x][new_y] == '.':
                matrix[new_x][new_y] = '@'
                matrix[x][y] = '.'
                x, y = new_x, new_y

            # if the next cell is a box, try to push it
            elif matrix[new_x][new_y] == 'O':
                if can_push_boxes(matrix, new_x, new_y, dx, dy):
                    push_boxes(matrix, new_x, new_y, dx, dy)

                    matrix[new_x][new_y] = '@'
                    matrix[x][y] = '.'
                    x, y = new_x, new_y

    return matrix


def calculate_gps_coordinates(matrix: list[list[str]]) -> int:
    box_coordinates = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'O':
                box_coordinates.append(100 * i + j)

    return sum(box_coordinates)


matrix, directions, robot_position = parse()
final_matrix = move_robot(matrix, directions, robot_position)
result = calculate_gps_coordinates(final_matrix)
print(f"sum of coordinates: {result}")

for row in final_matrix:
    print(''.join(row))
