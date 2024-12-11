import os


def read_lines() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


def blinking(numbers: list[int], n: int) -> list[int]:
    def split(number: int) -> list[int]:
        if number == 0:
            return [1]

        number_str = str(number)
        if len(number_str) % 2 == 0:
            half = len(number_str) // 2
            return [int(number_str[:half]), int(number_str[half:])]

        return [number * 2024]

    if n == 0:
        return numbers

    new_numbers = []
    for _, v in enumerate(numbers):
        new_numbers.extend(split(v))

    return blinking(new_numbers, n - 1)


lines = read_lines()
numbers = [int(num) for num in lines[0].split(' ')]

result = blinking(numbers, 25)
print(len(result))
