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


def read_input():
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        inputs = f.readlines()
    return inputs


lines = read_lines()


def get_destination(source, map_name):
    destination = source
    for destination_start, source_start, num in maps[map_name]:
        if source_start <= source and source <= source_start + num - 1:
            destination = source + destination_start - source_start
            return destination

    return destination


def get_data():
    # join lines into one string
    categories = "".join(lines).split("\n\n")

    seeds = [int(x) for x in categories[0].split(": ")[-1].split()]
    for name in categories[1::]:
        header, data = name.split(":\n")
        map_name, _ = header.split()
        maps[map_name] = []
        for line in data.split("\n"):
            maps[map_name].append([int(x) for x in line.split()])

    locations = []
    for seed in seeds:
        # print(f"Seed: {seed}")
        destination = seed
        for category_name, mapping in maps.items():
            destination = get_destination(destination, category_name)

        locations.append(destination)
        # print(f"{category_name}: {destination}")

    print(f"Lowest location: {min(locations)}")
    return locations


seeds = []
maps = {}

num = get_data()
print(num)
