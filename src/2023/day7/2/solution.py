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

labels = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

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
    cards = ''.join(sorted(cards, reverse=True,))
    groups = []
    group_size = 1
    current_card = cards[0]
    for card in cards[1::]:
        if card == current_card:
            group_size += 1
        else:
            groups.append(group_size)
            group_size = 1
        current_card = card
    groups.append(group_size)

    num_groups = len(groups)
    biggest_group = max(groups)
    if num_groups == 1:
        return 1
    elif num_groups == 2:
        if biggest_group == 4:
            return 2
        else:
            return 3
    elif num_groups == 3:
        if biggest_group == 3:
            return 4
        else:
            return 5
    elif num_groups == 4:
        return 6
    else:
        return 7



for line in lines:
    cards, bid = line.split()

    hand_type = 7
    if 'J' in cards:
        replacements = labels[:-1]
        for replacement in replacements:
            joker_cards = cards.replace('J', replacement)
            hand_type = min(hand_type, determine_type(joker_cards))
            if hand_type == 1:
                break
    else:
        hand_type = determine_type(cards)
    hands.append((cards, bid, hand_type))

hands = sorted(hands,
               reverse=True,
               key=lambda x: (x[2], labels.index(x[0][0]), labels.index(x[0][1]), labels.index(x[0][2]), labels.index(x[0][3]), labels.index(x[0][4])))

winnings = 0
for rank, hand in enumerate(hands):
    winnings += int(hand[1]) * (rank + 1)
    # print(f"Hand: {hand} rank: {rank + 1} bid: {hand[1]}")

print(f"Winnings: {winnings}")