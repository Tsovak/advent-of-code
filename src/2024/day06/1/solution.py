import os


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


def step_guard(matrix):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    row_len, col_len = len(matrix), len(matrix[0])

    # initial guard position and direction
    guard = next((
        (i, j, 0)
        for i in range(row_len)
        for j in range(col_len)
        if matrix[i][j] == "^"
    ))

    # save visited positions
    visited = set()
    visited.add(guard[:2])

    current_pos = guard

    while True:
        x, y, direction = current_pos

        nx = x + dx[direction]
        ny = y + dy[direction]

        # out of bounds
        if (
                nx < 0 or nx >= row_len or
                ny < 0 or ny >= col_len
        ):
            break

        if matrix[nx][ny] == '#':
            # turn right
            direction = (direction + 1) % 4
            current_pos = (x, y, direction)
        else:
            # go to the new position
            visited.add((nx, ny))
            current_pos = (nx, ny, direction)

    return len(visited)


lines = read_lines()
matrix = [list(line) for line in lines]

result = step_guard(matrix)
print(result)
