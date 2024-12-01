import os
from array import *

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


def closed_range(start, stop, step=1):
    dir = 1 if (step > 0) else -1
    return range(start, stop + dir, step)


def get_data():
    winnings = []
    my_cards = []

    for i, line in enumerate(lines):
        split = line.split(":")
        if len(split) != 2:
            print("error", split)
            exit(1)

        split = split[1].strip().split("|")
        if len(split) != 2:
            print("error", split)
            exit(1)

        winning = split[0].replace("  ", " ")
        my_card = split[1].replace("  ", " ")
        _winning = [int(x.strip()) for x in winning.strip().split(" ")]
        _my_card = [int(x.strip()) for x in my_card.strip().split(" ")]
        winnings.append(_winning)
        my_cards.append(_my_card)

    return winnings, my_cards


winnings, my_cards = get_data()


def count_winnings() -> dict:
    scores = {}

    length = len(winnings)
    for i in range(length):
        winning = winnings[i]
        my_card = my_cards[i]
        score = 0
        for j in range(len(winning)):
            if winning[j] in my_card:
                score += 1

        if score > 0:
            card_id = i + 1
            scores[card_id] = score
        print("score = ", score)

    return scores


scores = count_winnings()


def calculate_score() -> {}:
    result = {}
    for i in range(0, len(my_cards)):
        result[i + 1] = []

    for idx, value in scores.items():
        result[idx] = [value]
#
# Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
# Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
# Your copy of card 2 also wins one copy each of cards 3 and 4.
# Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
# Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
# Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
# Your one instance of card 6 (one original) has no matching numbers and wins no more cards.
#




    for card_id, value in scores.items():
        k = 0
        l = value
        while k < l:
            next_card = k + 1 + card_id
            next = result[next_card]
            if next:
                result[card_id].extend(next)
            k += 1

    return result


num = calculate_score()
sum = sum_numbers(num)
print(sum)
