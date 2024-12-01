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


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


steps = lines[0].strip()


def create_nodes_from_text():
    nodes_dict = {}

    for line in lines[1:]:
        # Ignore empty lines
        if line.strip() == '':
            continue
        line = line.strip()
        # Split the line on ' = ' to get the node name and its children
        node_name, children_text = line.split(' = ')

        # Get rid of parentheses and split on ', ' to get left and right child
        children_text = children_text.strip('()')
        left_child, right_child = children_text.split(', ')

        if left_child not in nodes_dict:
            nodes_dict[left_child] = Node(left_child)
        if right_child not in nodes_dict:
            nodes_dict[right_child] = Node(right_child)

        if node_name not in nodes_dict:
            nodes_dict[node_name] = Node(node_name, nodes_dict[left_child], nodes_dict[right_child])
        else:
            nodes_dict[node_name].left = nodes_dict[left_child]
            nodes_dict[node_name].right = nodes_dict[right_child]

    return nodes_dict


nodes = create_nodes_from_text()
fist_node = nodes['AAA']
node = fist_node
depth = 0

step_index = 0


def get_next_step() -> str:
    global step_index
    result = steps[step_index]
    step_index += 1
    if step_index >= len(steps):
        step_index = 0
    return result


def walk():
    global node
    global depth
    while node.value != 'ZZZ':
        step = get_next_step()
        if step == 'L':
            node = node.left
        else:
            node = node.right
        depth += 1

    print(f"Found ZZZ at depth {depth}")
    return


walk()

print(depth)
