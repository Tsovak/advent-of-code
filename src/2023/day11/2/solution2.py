import re
import os
from itertools import combinations

import numpy as np
from tqdm import tqdm

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


def repeat_column(array, column_id, times):
    n = 10
    for i in tqdm(range(n)):
        repeated_column = np.repeat(array[:, column_id:column_id + 1], times / n, axis=1)
        array = np.hstack((array[:, :column_id + 1], repeated_column, array[:, column_id + 1:]))
    return array


def repeat_row(array, row_id, times):
    n = 10
    for i in tqdm(range(n)):
        repeated_row = np.repeat(array[row_id:row_id + 1, :], times / n, axis=0)
        array = np.vstack((array[:row_id + 1, :], repeated_row, array[row_id + 1:, :]))
    return array

def extend_matrix_vertically(_matrix2d):
    for c, i in tqdm(enumerate(reversed(v_idx))):
        print("extend_matrix_vertically: column", c, "index", i)
        _matrix2d = repeat_column(_matrix2d, i, XXX - 1)

    return _matrix2d


def extend_matrix_horizontally(__matrix2d):
    for r, i in tqdm(enumerate(reversed(h_idx))):
        print("extend_matrix_horizontally: row", r, "index", i)
        __matrix2d = repeat_row(__matrix2d, i, XXX - 1)

    return __matrix2d


matrix2d = []
for row in matrix:
    matrix2d.append(list(row))

matrix2d = np.array(matrix2d)

print("extended matrix horizontally")
# matrix2d = extend_matrix_horizontally(matrix2d)
print("extended matrix vertically")
# matrix2d = extend_matrix_vertically(matrix2d)


def find_net_coodinates():
    net_coordinates = []
    for i, row in enumerate(matrix2d):
        for j, col in enumerate(row):
            if col == "#":
                net_coordinates.append((i, j))
    return net_coordinates


print("find net coordinates with numpy")
coords = np.where(matrix2d == "#")
net_coordinates = list(zip(coords[0], coords[1]))

print("find all pairs")
pairs = list(combinations(net_coordinates, 2))


# print(pairs)


# find the distance between each pair
# for each pair, find the distance between them
def calculate_distance(pair):
    (x1, y1), (x2, y2) = pair
    # check if coordinates inside v_idx or h_idx indexes. I want to increase column and row by XXX times every index in v_idx and h_idx
    # find all elements grater than x y in v_idx and h_idx
    # xx1 = [i for i in v_idx if i > x1]
    # yy1 = [i for i in h_idx if i > y1]
    #
    # xx2 = [i for i in v_idx if i < x2]
    # yy2 = [i for i in h_idx if i < y2]

    return (XXX-1)*(abs(x1 - x2) + abs(y1 - y2))


print("calculate distances")
distances = [calculate_distance(pair) for pair in pairs]
# print(distances)

# sum the distances
s = sum(distances)
print(s)
# 9799681
