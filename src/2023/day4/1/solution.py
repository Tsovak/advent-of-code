import os

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
    # Card   1: 30 51 48 31 36 33 49 83 86 17 | 17 33 31 70 90 37 86 45 58 21 83 52 59 68 55 32 20 43 48 75 30 42 80 60 71
    # Card   2: 83 45 32 60 10 94 13 29 52 43 | 47 15 94 32 13 64  4 48 20 83 52 75 41 50 60 14 45 43 37 29 35 10 89 77 25

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
        # get number list from string
        try:
            _winning = [int(x.strip()) for x in winning.strip().split(" ")]
            _my_card = [int(x.strip()) for x in my_card.strip().split(" ")]
            winnings.append(_winning)
            my_cards.append(_my_card)
        except:
            print("error", split)
            exit(1)

    return winnings, my_cards


def get_numbers() -> []:
    numbers = []
    return numbers


winnings, my_cards = get_data()


def count_winnings() -> []:
    scores = []
    length = len(winnings)
    for i in range(length):
        winning = winnings[i]
        my_card = my_cards[i]
        score = 0
        for j in range(len(winning)):
            if winning[j] in my_card:
                score += 1

        if score > 0:
            scores.append(score)
        print(score)

    return scores


scores = count_winnings()


def calculate_score() -> []:
    s = []

    for i in range(len(scores)):
        score = scores[i] - 1
        res = 2 ** score
        s.append(res)

    return s


num = calculate_score()
sum = sum_numbers(num)
print(sum)
