import os


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


lines = read_lines()
matrix = [list(line) for line in lines]


def split_matrix_into_regions(matrix: list[list[str]]):
    regions = []
    visited = set()

    def dfs(x, y, character, region):
        if not (0 <= x < len(matrix) and 0 <= y < len(matrix[0])) or matrix[x][y] != character or (x, y) in visited:
            return

        visited.add((x, y))
        region.append((x, y))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            dfs(new_x, new_y, character, region)

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            region = []
            dfs(x, y, matrix[x][y], region)
            if region:
                regions.append(region)

    return regions


def compact_result(result):
    regions = []
    for i, region in enumerate(result):
        if not region:
            continue
        tmp_matrix = [["." for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        x, y = region[0]
        letter = matrix[x][y]
        for x, y in region:
            tmp_matrix[x][y] = letter

        tmp_matrix = [row for row in tmp_matrix if not all([c == "." for c in row])]
        tmp_matrix = [row for row in zip(*tmp_matrix) if not all([c == "." for c in row])]
        regions.append(tmp_matrix)

    return regions


def print_result(result, compacted):
    for region in result:
        print(region)

    for region in compacted:
        print("\n".join(["".join(row) for row in region]))


def find_perimeter(matrix):
    perimeter = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] != ".":
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x, new_y = x + dx, y + dy
                    if not (0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0])) or matrix[new_x][new_y] == ".":
                        perimeter += 1

    return perimeter


def find_area(matrix):
    area = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] != ".":
                area += 1

    return area


result = split_matrix_into_regions(matrix)
compacted = compact_result(result)
# print_result(result, compacted)

perimeters = [find_perimeter(region) for region in compacted]
areas = [find_area(region) for region in compacted]
total_price = sum([perimeter * area for perimeter, area in zip(perimeters, areas)])
print(total_price)
