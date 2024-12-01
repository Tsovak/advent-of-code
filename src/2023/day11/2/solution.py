import re
import os
from itertools import combinations

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

XXX = 1000000

def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    # convert bytes to string
    lines = [line.decode("utf-8").strip() for line in lines]
    return lines


def read_file_into_matrix():
    with open(os.path.join(ROOT_DIR, 'data.txt'), "r") as file:
        return [line.strip() for line in file]


lines = read_lines()

matrix = read_file_into_matrix()

print(matrix)


def get_vertical_index():
    # iterate vertically. find column that contains only dots
    vertical_index = []
    for i in range(len(matrix[0])):
        column = [row[i] for row in matrix]
        if column.count(".") == len(column):
            vertical_index.append(i)

    return vertical_index


def get_horizontal_index():
    # iterate horizontally. find row that contains only dots
    horizontal_index = []
    for i in range(len(matrix)):
        row = matrix[i]
        if row.count(".") == len(row):
            horizontal_index.append(i)

    return horizontal_index


v_idx = get_vertical_index()
h_idx = get_horizontal_index()

print(v_idx)
print(h_idx)


def extend_matrix_horizontally():
    new_matrix = []
    # extend matrix in index h_idx row and in index v_idx column
    for i, row in enumerate(matrix):
        if i in h_idx:
            for j in range(XXX):
                new_matrix.append(row)
        else:
            new_matrix.append(row)
    return new_matrix


# matrix = extend_matrix_horizontally()


def duplicate_column(__matrix, column_index):
    for row in __matrix:
        # Duplicate the specified column
        row.insert(column_index, row[column_index])
    return __matrix


def extend_matrix_vertically():
    matrix2d = []
    for row in matrix:
        matrix2d.append(list(row))

    # k=0
    # for c, i in enumerate(v_idx):
    #     for j in range(XXX-1):
    #         matrix2d = duplicate_column(matrix2d, i + (k*(XXX-1)))
    #     k += 1

    return matrix2d


# matrix2d = extend_matrix_vertically()

# for row in matrix2d:
#     print("".join(row))
matrix2d = []
for row in matrix:
    matrix2d.append(list(row))


def find_net_coodinates():
    net_coordinates = []
    for i, row in enumerate(matrix2d):
        for j, col in enumerate(row):
            if col == "#":
                net_coordinates.append((i, j))
    return net_coordinates


net_coordinates = find_net_coodinates()
# print(net_coordinates)

pairs = list(combinations(net_coordinates, 2))
# print(pairs)


# find the distance between each pair
# for each pair, find the distance between them
def calculate_distance(pair):
    (x1, y1), (x2, y2) = pair
    return abs(x1 - x2) + abs(y1 - y2)


distances = [calculate_distance(pair) for pair in pairs]
# print(distances)

# sum the distances
s = sum(distances)
print(s)
# 9799681