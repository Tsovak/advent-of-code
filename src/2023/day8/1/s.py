import re
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    # convert bytes to string
    lines = [line.decode("utf-8") for line in lines]
    return lines


lines = read_lines()

instructions = []
node_dict = {}

instruction_index = 0


def get_next_instruction() -> int:
    global instruction_index
    result = instructions[instruction_index]
    instruction_index += 1
    if instruction_index >= len(instructions):
        instruction_index = 0
    return result


instructions_string, nodes_string = "".join(lines).split('\n\n')
instructions_string = instructions_string.replace(
    'L', '0').replace('R', '1')
instructions = [int(i) for i in instructions_string]

for line in nodes_string.splitlines():
    key, values = line.split(' = ')
    values = values.replace('(', '').replace(')', '')
    nodes = values.split(', ')
    node_dict[key] = nodes

steps = 0
node = 'AAA'

while node != 'ZZZ':
    next_instruction = get_next_instruction()
    node = node_dict[node][next_instruction]
    steps += 1

print(f"Steps needed: {steps}")
