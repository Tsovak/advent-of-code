import re
import os
from itertools import combinations

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    # convert bytes to string
    lines = [line.decode("utf-8").strip() for line in lines]
    return lines


def read_file_into_matrix():
    with open(os.path.join(ROOT_DIR, 'data.txt'), "r") as file:
        return [list(line.strip()) for line in file]


lines = read_lines()
"""Day 12"""
from functools import cache
from itertools import product
from typing import Generator, NamedTuple


class SpringInfo(NamedTuple):
    state: tuple[str, ...]
    sizes: tuple[int, ...]


InputData = list[SpringInfo]


def parse_input(path: str) -> InputData:
    with open(path, "r") as fin:
        data = []
        for line in fin.readlines():
            state_raw, sizes_raw = line.strip().split(" ")
            sizes = tuple(int(s) for s in sizes_raw.split(","))
            data.append(SpringInfo(state=tuple(state_raw), sizes=sizes))

        return data


def solve_part_one(data: InputData) -> int:
    answer = 0

    for spring_info in data:
        # answer += naive_solve(spring_info)
        answer += efficient_solve(spring_info.state, spring_info.sizes)

    return answer


@cache
def efficient_solve(state: tuple[str, ...], sizes: tuple[int, ...]) -> int:
    num_arrangements = 0

    max_pos = (
        len(state)
        - sizes[0]  # We need to fit the current spring
        - (sum(sizes[1:]) + len(sizes) - 1)  # We need to fit the remaining springs and separators "."
    )

    for pos in range(max_pos + 1):
        pattern = "." * pos + "#" * sizes[0] + "."

        if matches_prefix(pattern, state):
            if len(sizes) == 1:  # Final spring
                # There are no springs in the remaining part
                if all(c != "#" for c in state[len(pattern):]):
                    num_arrangements += 1
            else:
                num_arrangements += efficient_solve(
                    state=state[len(pattern):],
                    sizes=sizes[1:],
                )

    return num_arrangements


def matches_prefix(spring_pattern: str, state: list[str]) -> bool:
    if (
        len(spring_pattern) > len(state)
        and any(c == "#" for c in state[len(spring_pattern):])
    ):
        return False

    return all(
        c1 == c2 or c2 == "?"
        for c1, c2 in zip(spring_pattern, state)
    )



def naive_solve(data: InputData) -> int:
    num_arrangements = 0
    for state in generate_arrangements(spring_info.state):
        if get_block_sizes(state) == spring_info.sizes:
            num_arrangements += 1

    return num_arrangements


def generate_arrangements(state: list[str]) -> Generator[list[str], None, None]:
    unknown_pos = [i for i, c in enumerate(state) if c == "?"]

    for fields in product([".", "#"], repeat=len(unknown_pos)):
        current_state = list(state)
        for pos, f in zip(unknown_pos, fields):
            current_state[pos] = f
        yield tuple(current_state)


def get_block_sizes(state: tuple[str]) -> tuple[int]:
    block_sizes = []

    block = ""
    for i in range(len(state)):
        if state[i] == ".":
            if block:
                block_sizes.append(len(block))
                block = ""
        elif state[i] == "#":
            block += "#"

    if block:
        block_sizes.append(len(block))

    return tuple(block_sizes)


def solve_part_two(data: InputData) -> int:
    expanded_data = []

    for spring_info in data:
        state = tuple('?'.join([''.join(spring_info.state)] * 5))
        sizes = tuple(list(spring_info.sizes) * 5)

        expanded_data.append(SpringInfo(state=state, sizes=sizes))

    answer = solve_part_one(expanded_data)

    return answer


def main():
    filename = os.path.join(ROOT_DIR, 'data.txt')
    data = parse_input(filename)

    answer_two = solve_part_two(data)
    print("Part 2:", answer_two)


if __name__ == "__main__":
    main()
