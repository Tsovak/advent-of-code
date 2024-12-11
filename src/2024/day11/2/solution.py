import os


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


def split(number: int) -> list[int]:
    if number == 0:
        return [1]

    number_str = str(number)
    if len(number_str) % 2 == 0:
        half = len(number_str) // 2
        return [
            int(number_str[:half]),
            int(number_str[half:])
        ]
    return [number * 2024]


def blinking(numbers: list[int], until: int) -> int:
    stones = {}
    for n in numbers:
        stones[n] = stones.get(n, 0) + 1

    for _ in range(until):
        new_stones = {}

        for n, count in stones.items():
            splits = split(n)
            for split_num in splits:
                new_stones[split_num] = new_stones.get(split_num, 0) + count

        stones = new_stones

    return sum(stones.values())


lines = read_lines()
numbers = [int(num) for num in lines[0].split(' ')]

total = blinking(numbers, 75)
print(total)
