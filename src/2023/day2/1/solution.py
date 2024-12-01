import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    return lines


lines = read_lines()

red_cubes = 12
green_cubes = 13
blue_cubes = 14

def get_ids() -> dict:
    data = {}

    for line in lines:
        line = line.decode("utf-8").strip()
        game_id, *colors = line.split(":")
        game_id = int(game_id.split(" ")[1])
        colors = [color.strip() for color in colors]
        data[game_id] = []
        for round in colors:
            round = round.split(";")
            for c in round:
                c = c.strip().replace(", ", ",")
                part = c.split(",")
                row = {}
                for p in part:
                    number = int(p.split(" ")[0])
                    color = p.split(" ")[1]
                    row[color] = number

                data[game_id].append(row)

    return data


def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)


data = get_ids()

def get_game_numbers():
    game_numbers = []
    for game_id, rounds in data.items():
        is_valid = True
        for round in rounds:
            if 'red' in round and round["red"] > red_cubes:
                is_valid = False
                break
            if 'green' in round and round["green"] > green_cubes:
                is_valid = False
                break
            if 'blue' in round and round["blue"] > blue_cubes:
                is_valid = False
                break
        if is_valid:
            game_numbers.append(game_id)

    return game_numbers


game_numbers = get_game_numbers()
sum = sum_numbers(game_numbers)
print(sum)