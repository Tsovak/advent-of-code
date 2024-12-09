import os


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


lines = read_lines()
line = lines[0]


# if len(line) % 2 != 0:
#     line += "0"


def disk_fragmenter(line):
    fragment = []
    for i, d in enumerate(line.strip()):
        blocks = int(d)
        file_id = i // 2 if i % 2 == 0 else None
        fragment += [file_id] * blocks

    left_idx = next(i for i, v in enumerate(fragment) if v is None)
    right_idx = next(i for i, v in reversed(list(enumerate(fragment))) if v is not None)

    while left_idx < right_idx:
        fragment[left_idx] = fragment[right_idx]
        fragment[right_idx] = None

        while fragment[left_idx] is not None:
            left_idx += 1
        while fragment[right_idx] is None:
            right_idx -= 1

    return sum(i * d for i, d in enumerate(fragment) if d is not None)


result = disk_fragmenter(line)
print(result)
