import re
import os
from itertools import pairwise

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.visited = set()
        self.max_distance = 0
        self.max_cell = (0, 0)
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Down, Left, Up
        self.dir = {
            '|': [(0, 1), (0, -1)],
            '-': [(1, 0), (-1, 0)],
            'L': [(0, 1), (-1, 0)],
            'J': [(0, 1), (1, 0)],
            '7': [(0, -1), (1, 0)],
        }

    def start(self, startx, starty):
        self.dfs(startx, starty, 0)
        return self.max_distance

    def dfs(self, row, col, distance):
        if (row, col) in self.visited:
            print("Cycle detected", "row:", row, "col:", col, "distance:", distance)
            exit(1)

        self.visited.add((row, col))

        if distance > self.max_distance:
            self.max_distance = distance
            self.max_cell = (row, col)

        char = self.grid[row][col]

        match char:
            case '|':
                dx = 1
                dy = 0
                new_row, new_col = row + dx, col + dy
                if self.is_valid(new_row, new_col):
                    self.dfs(new_row, new_col, distance + 1)
            case '-':
                dx = 0
                dy = 1
                new_row, new_col = row + dx, col + dy
                if self.is_valid(new_row, new_col):
                    self.dfs(new_row, new_col, distance + 1)
            case 'L':

    def is_valid(self, row, col):
        if row < 0 or col < 0 or row > len(self.grid) - 1 or col > len(self.grid[0]) - 1:
            return False
        if self.grid[row][col] == '.':
            return False
        return True


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    # convert bytes to string
    lines = [line.decode("utf-8").strip() for line in lines]
    return lines


lines = read_lines()


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

def find_s_index() -> tuple[int, int]:
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == 'S':
                return i, j


# i = len(lines) - 1
# j = len(lines[0]) - 1


# replace the starting position
# lines[i][j] = 0

grid = [list("..F7."),
        list(".FJ|."),
        list("SJ.L7"),
        list("|F--J"),
        list("LJ...")]

g = Grid(grid)
g.start()
print(g.max_distance)

# def maxDistance(start, matrix):
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     visited = set()
#     stack = [(start, 0)]
#     max_distance = 0
#
#     def is_valid(i, j):
#         return 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] != "." and (i, j) not in visited
#
#     while stack:
#         (i, j), distance = stack.pop()
#         max_distance = max(max_distance, distance)
#         for direction in directions:
#             ni, nj = i + direction[0], j + direction[1]
#             if is_valid(ni, nj):
#                 visited.add((ni, nj))
#                 stack.append(((ni, nj), distance + 1))
#
#     return max_distance


# # Define the grid here
# grid = [list("..F7."),
#         list(".FJ|."),
#         list("SJ.L7"),
#         list("|F--J"),
#         list("LJ...")]
#
# grid = lines
#
# start_idx = find_s_index()
# print(maxDistance(start_idx, grid))
