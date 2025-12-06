import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    return lines


lines = read_lines()

matrix = []
for line in lines:
    line = line.decode("utf-8").strip()
    parts = [p for p in line.split(" ") if p != "" ]
    matrix.append(parts)

col_len = len(matrix[0])
operations = matrix[-1]

total = 0
for i in range(col_len):
    col = [row[i] for row in matrix[:-1]]
    match operations[i]:
        case "+":
            summed = sum(int(x) for x in col)
            total += summed
        case "*":
            mltp = 1
            for x in col:
                mltp *= int(x)
            total += mltp

print(total)