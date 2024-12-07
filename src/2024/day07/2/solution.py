import os
from itertools import product


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


lines = read_lines()

items = [
    (line.split(': ')[0], [int(num) for num in line.split(': ')[1].split()])
    for line in lines
]

allowed_operations = ['*', '+', '||']


def evaluate_expression(numbers, ops):
    result = numbers[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))

    return result


def find_valid_equations(desired_sum: int, numbers):
    valid_equations = []

    op_combinations = list(product(allowed_operations, repeat=len(numbers) - 1))

    for ops in op_combinations:
        try:
            result = evaluate_expression(numbers, ops)
            if result == desired_sum:
                valid_equations.append(ops)
        except:
            continue

    return valid_equations


total_calibration = 0
for item in items:
    desired_sum, numbers = item
    desired_sum = int(desired_sum)
    valid_equations = find_valid_equations(desired_sum, numbers)
    if valid_equations:
        total_calibration += int(desired_sum)

print(total_calibration)
