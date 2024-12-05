import os

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

result = sum(
    update[len(update) // 2]
    for update in updates
    if update not in unsorted
)

print(result)
