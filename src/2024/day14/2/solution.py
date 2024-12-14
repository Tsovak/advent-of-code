import os


def read_input() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


def parse_robot(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    pos, vel = line.split(' v=')
    px, py = map(int, pos.replace('p=', '').split(','))
    vx, vy = map(int, vel.split(','))
    return (px, py), (vx, vy)


def wrap_coordinate(coord: int, max_size: int) -> int:
    return coord % max_size


def simulate_robots(robots: list[tuple[tuple[int, int], tuple[int, int]]],
                    duration: int,
                    width: int,
                    height: int) -> list[tuple[int, int]]:
    final_positions = []

    for (x, y), (vx, vy) in robots:
        final_x = wrap_coordinate(x + vx * duration, width)
        final_y = wrap_coordinate(y + vy * duration, height)
        final_positions.append((final_x, final_y))

    return final_positions


def find_easter_egg_time(robots: list[tuple[tuple[int, int], tuple[int, int]]],
                         width: int,
                         height: int,
                         max_duration: int = 1_000_000) -> int:
    max_neighbors = 0
    easter_egg_time = -1

    for duration in range(max_duration):
        positions = simulate_robots(robots, duration, width, height)
        positions_set = set(positions)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        neighbors_count = sum(
            (x + dx, y + dy) in positions_set
            for (x, y) in positions_set
            for (dx, dy) in directions
        )

        if neighbors_count > max_neighbors:
            max_neighbors = neighbors_count
            easter_egg_time = duration

            if duration % 1000 == 0 or neighbors_count > width * height * 0.3:
                matrix = [[0] * width for _ in range(height)]
                for x, y in positions:
                    matrix[y][x] += 1

                print(f"time: {duration}")
                print(f"neighbors: {neighbors_count}")
                for row in matrix:
                    print(''.join(['#' if x else '.' for x in row]))
                print()

        if neighbors_count > width * height * 0.3:
            return duration

    return easter_egg_time


WIDTH = 101
HEIGHT = 103

lines = read_input()
robots = [parse_robot(line) for line in lines]

result = find_easter_egg_time(robots, WIDTH, HEIGHT)
print(f"configuration time: {result}")
