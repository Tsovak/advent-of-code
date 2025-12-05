import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    return lines


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []

    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def freshness_count(ids: list[int], ranges: list[tuple[int, int]]) -> int:
    count = 0
    for id in ids:
        for start, end in ranges:
            if start <= id <= end:
                count += 1
                break
    return count

lines = read_lines()

ranges = []
ids = []
for line in lines:
    line = line.decode("utf-8").strip()
    parts = line.split("-")
    if len(parts) == 2:
        ranges.append((int(parts[0]), int(parts[1])))
    elif len(parts) == 1 and parts[0] != "":
        ids.append(int(parts[0]))

print(freshness_count(ids, merge_ranges(ranges)))