import os
from concurrent.futures import ProcessPoolExecutor

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


def get_destination(source, map_name):
    destination = source
    for destination_start, source_start, num in maps[map_name]:
        if source_start <= source and source <= source_start + num - 1:
            destination = source + destination_start - source_start
            return destination

    return destination


def task(args):
    seed_start, seed_range, _maps = args
    min_location = 9999999999999999999999

    print(f"Seed start: {seed_start}, seed range: {seed_range}")

    for seed in range(seed_start, seed_start + seed_range):
        # print(f"Seed: {seed}")
        destination = seed
        for category_name, mapping in _maps.items():
            destination = get_destination(destination, mapping)
            # print(f"{category_name}: {destination}")

        min_location = min(min_location, destination)

    return min_location


def get_data():
    categories = "".join(lines).split("\n\n")
    seeds = [int(x) for x in categories[0].split(": ")[-1].split()]
    for name in categories[1::]:
        header, data = name.split(":\n")
        map_name, _ = header.split()
        maps[map_name] = []
        for line in data.split("\n"):
            maps[map_name].append([int(x) for x in line.split()])

    min_location = 9999999999999999999999
    with ProcessPoolExecutor(max_workers=10) as executor:
        # with ThreadPool(processes=2) as pool:
        seed_data = [(seed_start, seed_range, maps) for seed_start, seed_range in zip(*[iter(seeds)] * 2)]
        # for seed_start, seed_range in zip(*[iter(seeds)]*2):
        for result in executor.map(task, seed_data):
            print(f"Result: {result}")
            min_location = min(result, min_location)

    print(f"Lowest location: {min_location}")
    return min_location


seeds = []
maps = {}

num = get_data()
print(num)
