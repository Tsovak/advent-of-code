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


def count_quadrant_robots(positions: list[tuple[int, int]],
                          width: int,
                          height: int) -> list[int]:
    quadrants = [0, 0, 0, 0]

    for x, y in positions:
        # ignore on the middle lines
        if x == width // 2 or y == height // 2:
            continue

        if x < width // 2 and y < height // 2:
            quadrants[0] += 1
        elif x > width // 2 and y < height // 2:
            quadrants[1] += 1
        elif x < width // 2 and y > height // 2:
            quadrants[2] += 1
        else:  # x > width // 2 and y > height // 2
            quadrants[3] += 1

    return quadrants


WIDTH = 101
HEIGHT = 103
DURATION = 100

lines = read_input()
robots = [parse_robot(line) for line in lines]

final_positions = simulate_robots(robots, DURATION, WIDTH, HEIGHT)

quadrant_counts = count_quadrant_robots(final_positions, WIDTH, HEIGHT)

safety_factor = quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3]

print(f"Quadrant Counts: {quadrant_counts}")
print(f"Safety Factor: {safety_factor}")
