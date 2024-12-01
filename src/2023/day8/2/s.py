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
from math import lcm

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


if __name__ == "__main__":
    instructions_string, nodes_string = "".join(lines).split('\n\n')
    instructions_string = instructions_string.replace(
        'L', '0').replace('R', '1')
    instructions = [int(i) for i in instructions_string]

    for line in nodes_string.splitlines():
        key, values = line.split(' = ')
        values = values.replace('(', '').replace(')', '')
        nodes = values.split(', ')
        node_dict[key] = nodes

    nodes = list(filter(lambda x: x[-1] == 'A', node_dict.keys()))
    all_steps = []

    for node in nodes:
        instruction_index = 0
        steps = 0
        while node[-1] != 'Z':
            next_instruction = get_next_instruction()
            node = node_dict[node][next_instruction]
            steps += 1
        all_steps.append(steps)

    least = lcm(*all_steps)

    print(f"Steps needed: {least}")
    print("all steps:", all_steps)
