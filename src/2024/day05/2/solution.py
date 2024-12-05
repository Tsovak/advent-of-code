import os

import networkx as nx

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


lines = read_lines()

separator_index = lines.index('')
rule_lines = lines[:separator_index]
update_lines = lines[separator_index + 1:]

rules = [tuple(map(int, l.split("|"))) for l in rule_lines]
updates = [tuple(map(int, l.split(","))) for l in update_lines]

unsorted = {
    update
    for update in updates
    if any(
        a in update and b in update and update.index(a) > update.index(b)
        for a, b in rules
    )
}

sorted_updates = [
    list(
        nx.topological_sort(
            nx.DiGraph(
                (a, b)
                for a, b in rules
                if a in update and b in update
            )
        )
    )
    for update in unsorted
]

result = sum(
    update[len(update) // 2]
    for update in sorted_updates
)

print(result)
