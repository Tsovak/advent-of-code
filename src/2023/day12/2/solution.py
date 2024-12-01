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

matrix = read_file_into_matrix()


# print(matrix)


# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1

# ???.### 1,1,3 - 1 arrangement
# .??..??...?##. 1,1,3 - 4 arrangements
# ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
# ????.#...#... 4,1,1 - 1 arrangement
# ????.######..#####. 1,6,5 - 4 arrangements
# ?###???????? 3,2,1 - 10 arrangements


# In the first line (???.### 1,1,3), there is exactly one way separate groups of one, one, and three broken springs (in that order) can appear in that row: the first three unknown springs must be broken, then operational, then broken (#.#), making the whole row #.#.###.
def prepare():
    data = []
    for line in lines:
        springs = line.split(' ')[0]
        groups = [int(x) for x in line.split(' ')[1].split(',')]
        data.append((springs, groups))
    return data


data = prepare()


# print(data)


def get_ideal_arrangement(groups):
    springs = ["#" * n for n in groups]
    return ".".join(springs)


def get_arrangements(springs, groups, pos=0):
    arrangements = []
    if get_ideal_arrangement(groups) == springs:
        arrangements.append(springs)
        return arrangements

    if len(groups) == 0 or len(springs) == 0:
        return arrangements

    g = groups[0]
    for i in range(pos, len(springs) - g + 1):
        if springs[i] == "?":
            if springs[i:i + g] == "#" * g:
                arrangements.append(springs[:i] + "." * g + springs[i + g:])

    return arrangements


arrangements = []


def generate_arrangements(springs, groups, pos=0):
    if pos == len(groups):
        return [springs] if '?' not in springs else []

    for i in range(len(springs)):
        if springs[i:i + groups[pos]] == '?' * groups[pos]:
            new_springs = springs[:i] + '#' * groups[pos] + springs[i + groups[pos] + 1:]
            arrangements.extend(generate_arrangements(new_springs, groups, pos + 1))
    return arrangements


def generate_arrangements2(springs, groups):
    if len(groups) == 0:  # plus de # à placer
        return 1 if '#' not in springs else 0
    if sum(groups) + len(groups) - 1 > len(springs):  # plus assez de place pour les #
        return 0

    # Récursion
    if springs[0] == '.':
        return generate_arrangements2(springs[1:], groups)

    nb = 0
    if springs[0] == '?':
        nb += generate_arrangements2(springs[1:], groups)

    if '.' not in springs[:groups[0]] and (len(springs) <= groups[0] or len(springs) > groups[0] and springs[groups[0]] != '#'):
        nb += generate_arrangements2(springs[groups[0] + 1:], groups[1:])

    return nb


def count_possibilities(springs: str, groups: list[int]) -> int:
    counts = {(-1, -1): 1}
    for group in groups:
        new_counts = {}
        positions = 0

    return 0


# lines = [
#     ("???.###", [1, 1, 3]),
#     (".??..??...?##.", [1, 1, 3]),
#     ("?#?#?#?#?#?#?#?", [1, 3, 1, 6]),
#     ("????.#...#...", [4, 1, 1]),
#     ("????.######..#####.", [1, 6, 5]),
#     ("?###????????", [3, 2, 1])
# ]

summ = 0
for springs, groups in data:
    summ += generate_arrangements2(springs, groups)

print(summ)
