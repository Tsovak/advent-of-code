import os


def read_input() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


def is_valid_pattern(patterns: list[str], design: str) -> bool:
    for pattern in patterns:
        if design.startswith(pattern):
            if is_valid_pattern(patterns, design[len(pattern):]):
                return True

    return design == ""


lines = read_input()
patterns = lines[0].split(", ")
design = lines[2:]

result = [d for d in design if is_valid_pattern(patterns, d)]
print(len(result))
