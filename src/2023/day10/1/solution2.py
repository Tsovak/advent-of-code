import os
from queue import Queue

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_NAME = 'data.txt'
DIRECTIONS_MAPPING = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
}
INITIAL_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
START_CHAR = 'S'
INVALID_CHARS = ["L", "7"]

def read_file_into_matrix():
    with open(os.path.join(ROOT_DIR, DATA_FILE_NAME), "r") as file:
        return [line.strip() for line in file]

def find_start_position(matrix):
    for y, line in enumerate(matrix):
        for x, char in enumerate(line):
            if char == START_CHAR:
                return x, y
    assert False, f"{START_CHAR} start position not found in matrix."

def calculate_distances(matrix, start_pos, directions_mapping, initial_directions):
    x, y = start_pos
    queue = Queue()
    for dir_x, dir_y in initial_directions:
        char = matrix[y + dir_y][x + dir_x]
        if char in directions_mapping:
            for dx, dy in directions_mapping[char]:
                if (x, y) == (x + dx + dir_x, y + dy + dir_y):
                    queue.put((1, (x + dir_x, y + dir_y)))
    distances = {start_pos: 0}
    while not queue.empty():
        distance, (x, y) = queue.get()
        if (x, y) in distances:
            continue
        distances[(x, y)] = distance
        for dx, dy in directions_mapping[matrix[y][x]]:
            queue.put((distance + 1, (x + dx, y + dy)))
    return distances

def calculate_inside_count(matrix, distances):
    width, height = len(matrix[0]), len(matrix)
    inside_count = 0
    for y, line in enumerate(matrix):
        for x, char in enumerate(line):
            if (x, y) in distances:
                continue
            crosses = 0
            x2, y2 = x, y
            while x2 < width and y2 < height:
                char2 = matrix[y2][x2]
                if (x2, y2) in distances and char2 not in INVALID_CHARS:
                    crosses += 1
                x2 += 1
                y2 += 1
            if crosses % 2 == 1:
                inside_count += 1
    return inside_count

matrix = read_file_into_matrix()
start_pos = find_start_position(matrix)
distances = calculate_distances(matrix, start_pos, DIRECTIONS_MAPPING, INITIAL_DIRECTIONS)
print(f"Part 1: {max(distances.values())}")
inside_count = calculate_inside_count(matrix, distances)
print(f"Part 2: {inside_count}")
