import re
import os
from collections import Counter

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    # convert bytes to string
    lines = [line.decode("utf-8") for line in lines]
    return lines


lines = read_lines()

labels = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

# (num_groups, biggest_group)
types = [
    (1, 5),  # Five of a kind
    (2, 4),  # Four of a kind
    (2, 3),  # Full house
    (3, 3),  # Three of a kind
    (3, 2),  # Two pair
    (4, 2),  # One pair
    (5, 1)  # High card
]

hands = []


def determine_type(cards):
    groups = Counter(cards).most_common()
    groups = [group[1] for group in groups]

    num_groups = len(groups)
    biggest_group = max(groups)

    hand_type = types.index((num_groups, biggest_group))
    return hand_type


for line in lines:
    cards, bid = line.split()
    hand_type = determine_type(cards)
    hands.append((cards, bid, hand_type))

hands = sorted(hands,
               reverse=True,
               key=lambda x: (
               x[2], labels.index(x[0][0]), labels.index(x[0][1]), labels.index(x[0][2]), labels.index(x[0][3]), labels.index(x[0][4])))

winnings = 0
for rank, hand in enumerate(hands):
    winnings += int(hand[1]) * (rank + 1)
    # print(f"Hand: {hand} rank: {rank + 1} bid: {hand[1]}")

print(f"Winnings: {winnings}")
