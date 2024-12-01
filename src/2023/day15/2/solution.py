import re
import os
from itertools import combinations

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    # convert bytes to string
    lines = [line.decode("utf-8") for line in lines]
    return lines


def read_file_into_matrix():
    with open(os.path.join(ROOT_DIR, 'data.txt'), "r") as file:
        return [list(line.strip()) for line in file]


lines = read_lines()
lines = "".join(lines)

boxes = []


def hash(input):
    current = 0
    for c in input:
        current += ord(c)
        current *= 17
        current = current % 256
    return current


for i in range(256):
    boxes.append({})

for step in lines.split(","):
    if "=" in step:
        label, focal = step.split("=")
        box_id = hash(label)

        boxes[box_id][label] = focal
    elif "-" in step:
        label, _ = step.split("-")
        box_id = hash(label)
        if label in boxes[box_id].keys():
            del boxes[box_id][label]

result = 0
for box_id, box in enumerate(boxes):
    for slot_id, (_, focal) in enumerate(box.items()):
        result += (box_id + 1) * (slot_id + 1) * int(focal)

print(result)