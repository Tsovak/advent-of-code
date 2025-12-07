import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.read().splitlines()

    return lines

def print_matrix(matrix: list[list[str]]) -> None:
    for row in matrix:
        print("".join(row))
    print()

def beaming(matrix: list[list[str]]) -> None:
    s = [ (i, j)
          for i in range(len(matrix))
          for j in range(len(matrix[0]))
          if matrix[i][j] == 'S'
          ]
    
    splitters = [ (i, j)
          for i in range(len(matrix))
          for j in range(len(matrix[0]))
          if matrix[i][j] == '^'
          ]
    print(s)
    print(splitters)
    s_i, s_j = s[0]
    matrix[s_i+1][s_j] = '|'
    for i in range(2, len(matrix)-1, 1):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '^' and matrix[i-1][j] == '|' and i < len(matrix) and j < len(matrix[0]):
                matrix[i+1][j-1] = '|'
                matrix[i+1][j+1] = '|'
            if matrix[i][j] == '|' and matrix[i+1][j] != '^' and i < len(matrix)-1:
                matrix[i+1][j] = '|'
    
    print_matrix(matrix)
    
    count = 0 
    for i, j in splitters:
        if matrix[i-1][j] == '|':
            count += 1
    print("Beamed splitters: ", count)


lines = read_lines()

matrix = []
for line in lines:
    line = line.decode("utf-8")
    parts = [l for l in line]
    matrix.append(parts)


beaming(matrix)