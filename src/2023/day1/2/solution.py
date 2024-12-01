import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    return lines


lines = read_lines()


def replace(line, exit=False):
    if exit:
        return line

    iniconfig_len = len(line)
    for idx in range(len(line)):
        match line[idx]:
            case "o":
                if line[idx:idx + 3] == "one":
                    line = line[:idx] + "1" + line[idx + 3:]
                    return replace(line)
                return replace(line, len(line) == iniconfig_len)
            case "t":
                if line[idx:idx + 3] == "two":
                    line = line[:idx] + "2" + line[idx + 3:]
                    return replace(line)
                elif line[idx:idx + 5] == "three":
                    line = line[:idx] + "3" + line[idx + 5:]
                    return replace(line)
                return replace(line, len(line) == iniconfig_len)
            case "f":
                if line[idx:idx + 4] == "four":
                    line = line[:idx] + "4" + line[idx + 4:]
                    return replace(line)
                elif line[idx:idx + 4] == "five":
                    line = line[:idx] + "5" + line[idx + 4:]
                    return replace(line)
                return replace(line, len(line) == iniconfig_len)
            case "s":
                if line[idx:idx + 3] == "six":
                    line = line[:idx] + "6" + line[idx + 3:]
                    return replace(line)
                elif line[idx:idx + 5] == "seven":
                    line = line[:idx] + "7" + line[idx + 5:]
                    return replace(line)
                return replace(line, len(line) == iniconfig_len)
            case "e":
                if line[idx:idx + 5] == "eight":
                    line = line[:idx] + "8" + line[idx + 5:]
                    return replace(line)
                return replace(line, len(line) == iniconfig_len)
            case "n":
                if line[idx:idx + 4] == "nine":
                    line = line[:idx] + "9" + line[idx + 4:]
                    return replace(line)
                return replace(line, len(line) == iniconfig_len)

    return line


def normalize_line(line):
    result = "_" + line + "_"
    result = "one1one".join(result.split("one"))
    result = "two2two".join(result.split("two"))
    result = "three3three".join(result.split("three"))
    result = "four4four".join(result.split("four"))
    result = "five5five".join(result.split("five"))
    result = "six6six".join(result.split("six"))
    result = "seven7seven".join(result.split("seven"))
    result = "eight8eight".join(result.split("eight"))
    result = "nine9nine".join(result.split("nine"))
    return result


def get_first_and_last_digit(line) -> tuple[int, int]:
    # digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

    # 53789
    # [29, 23, 13, 14, 42, 14, 76]

    line = replace(line.decode("utf-8"))
    all_ints = [int(i) for i in line if i.isdigit()]

    first = all_ints[0]
    last = all_ints[-1]

    return first, last


def get_all_numbers(lines: list[str]) -> list[int]:
    numbers = []

    for line in lines:
        first, last = get_first_and_last_digit(line)
        res = first * 10 + last
        numbers.append(res)

    print(numbers)
    return numbers


def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)


numbers = get_all_numbers(lines)
result = sum_numbers(numbers)
print(result)

rgxjrsldrfmzq25szhbldzqhrhbjpkbjlsevenseven
slkjvk4threesevenznjqmmfive

## [91, 57, 81, 79, 28, 41, 41, 27, 45, 61, 17, 82, 27, 72, 45, 76, 32, 22, 13, 88, 15, 67, 85, 75, 55, 25, 75, 76, 72, 41, 58, 51, 13, 82, 73, 22, 73, 86, 32, 71, 92, 15, 49, 91, 17, 18, 32, 99, 77, 92, 38, 53, 25, 97, 22, 28, 84, 65, 28, 94, 47, 68, 63, 36, 66, 71, 51, 35, 91, 54, 43, 44, 18, 71, 96, 21, 37, 17, 27, 86, 38, 96, 16, 23, 51, 44, 72, 55, 71, 97, 82, 79, 99, 62, 88, 11, 88, 71, 65, 42, 61, 53, 33, 61, 39, 23, 24, 96, 24, 19, 65, 48, 11, 79, 38, 13, 13, 48, 21, 77, 55, 39, 32, 22, 16, 22, 64, 95, 96, 43, 29, 71, 22, 89, 29, 18, 91, 98, 43, 65, 11, 74, 63, 11, 74, 56, 41, 82, 38, 18, 71, 64, 96, 19, 81, 99, 13, 88, 95, 43, 15, 33, 46, 22, 87, 52, 29, 69, 92, 11, 17, 11, 96, 22, 96, 34, 32, 54, 43, 79, 56, 88, 51, 91, 71, 91, 37, 35, 66, 87, 71, 16, 14, 25, 16, 66, 98, 29, 31, 98, 87, 33, 18, 63, 62, 11, 88, 56, 66, 92, 18, 26, 94, 62, 58, 42, 19, 41, 64, 61, 52, 17, 92, 38, 79, 19, 95, 32, 35, 15, 96, 89, 67, 57, 53, 13, 36, 48, 89, 38, 71, 55, 55, 21, 85, 17, 55, 23, 28, 87, 77, 34, 39, 92, 19, 94, 72, 27, 37, 21, 22, 73, 57, 29, 42, 73, 64, 85, 64, 21, 72, 31, 54, 82, 65, 11, 22, 53, 28, 12, 94, 12, 62, 96, 47, 31, 74, 37, 33, 84, 42, 77, 28, 17, 34, 47, 42, 87, 36, 74, 98, 38, 49, 26, 28, 14, 23, 59, 88, 11, 15, 45, 85, 53, 19, 37, 86, 14, 52, 64, 48, 85, 71, 79, 11, 11, 79, 89, 89, 31, 56, 48, 95, 75, 63, 72, 89, 88, 58, 78, 47, 42, 15, 48, 77, 36, 85, 68, 93, 73, 52, 82, 58, 34, 22, 12, 86, 35, 91, 19, 13, 44, 95, 52, 58, 51, 65, 13, 61, 13, 87, 69, 63, 45, 24, 47, 42, 49, 28, 61, 21, 33, 99, 27, 65, 24, 74, 73, 74, 72, 29, 87, 94, 29, 88, 53, 24, 77, 45, 33, 64, 89, 16, 68, 92, 36, 98, 16, 78, 53, 27, 26, 34, 47, 88, 49, 23, 52, 88, 91, 99, 87, 62, 66, 88, 67, 57, 59, 61, 48, 69, 57, 55, 99, 22, 26, 45, 17, 63, 38, 74, 23, 17, 93, 63, 23, 91, 94, 54, 67, 55, 89, 57, 67, 89, 79, 29, 31, 48, 73, 48, 29, 17, 51, 44, 82, 72, 53, 12, 21, 11, 33, 56, 61, 53, 32, 98, 59, 66, 86, 46, 14, 89, 14, 11, 29, 79, 95, 67, 76, 88, 99, 42, 49, 53, 18, 35, 19, 33, 75, 64, 77, 24, 97, 41, 83, 94, 23, 99, 15, 24, 61, 72, 63, 44, 72, 13, 25, 64, 43, 28, 44, 37, 27, 53, 91, 95, 75, 66, 61, 38, 38, 54, 87, 96, 71, 29, 25, 81, 13, 11, 58, 74, 38, 32, 96, 35, 88, 34, 63, 75, 61, 41, 11, 11, 91, 39, 56, 77, 77, 77, 23, 87, 89, 17, 47, 55, 98, 52, 27, 91, 98, 87, 67, 35, 35, 15, 78, 19, 85, 17, 41, 23, 52, 97, 19, 68, 39, 43, 44, 27, 12, 86, 23, 87, 28, 49, 83, 92, 62, 72, 24, 23, 56, 18, 58, 32, 17, 11, 15, 77, 33, 84, 47, 73, 95, 82, 48, 43, 97, 35, 12, 13, 95, 27, 57, 67, 34, 88, 33, 99, 39, 97, 33, 62, 76, 63, 14, 84, 71, 52, 21, 37, 93, 48, 57, 29, 73, 14, 68, 19, 33, 97, 29, 86, 22, 92, 64, 42, 27, 66, 62, 22, 43, 68, 82, 44, 95, 74, 75, 37, 15, 89, 81, 43, 61, 53, 34, 45, 86, 31, 55, 43, 92, 88, 94, 87, 54, 41, 34, 45, 22, 63, 44, 23, 47, 54, 97, 18, 14, 77, 36, 48, 89, 49, 97, 71, 73, 41, 83, 91, 48, 89, 39, 97, 88, 28, 73, 61, 11, 62, 12, 24, 76, 22, 96, 18, 95, 56, 55, 17, 98, 61, 78, 73, 45, 94, 16, 65, 15, 88, 62, 57, 55, 91, 28, 99, 31, 61, 27, 79, 34, 64, 99, 42, 22, 13, 66, 37, 28, 22, 45, 65, 36, 77, 84, 14, 11, 29, 64, 97, 45, 96, 65, 18, 84, 29, 87, 32, 75, 89, 33, 17, 11, 39, 56, 79, 42, 75, 49, 72, 93, 39, 58, 16, 19, 36, 65, 44, 64, 52, 24, 16, 38, 74, 59, 38, 56, 65, 73, 72, 24, 27, 23, 11, 26, 82, 92, 82, 88, 79, 98, 44, 78, 91, 35, 14, 59, 58, 77, 98, 95, 95, 51, 15, 64, 46, 64, 38, 24, 85, 59, 17, 15, 62, 95, 22, 88, 14, 12, 52, 82, 22, 52, 83, 46, 55, 52, 22, 83, 54, 68, 53, 31, 26, 55, 35, 38, 58, 24, 33, 85, 81, 95, 32, 83, 54, 71, 71, 65, 45, 74, 96, 88, 33, 39, 14, 14, 71, 96, 43, 18, 56, 16, 66, 79, 23, 15, 54, 17, 85, 97, 23, 65, 94, 97, 59, 24, 66, 49, 31, 19, 19, 49, 66, 82, 75, 18, 86, 66, 98, 24, 44, 63, 63, 46, 33, 36, 97, 24, 47, 83, 74, 52, 95, 83, 52, 74, 11, 54, 49, 63, 88, 71, 54, 29, 55, 98, 56, 31, 48, 32, 71, 68, 11, 69, 86, 96, 49, 25, 33, 51, 91, 52, 48, 34, 37, 55, 48, 81, 48, 43, 69, 44, 49, 64, 94, 67, 99, 58, 86, 72, 78, 87, 46, 53, 27, 66, 89, 51, 42, 68, 47, 32, 57, 43, 72, 97, 87, 29]
## [91, 57, 81, 79, 28, 41, 41, 25, 44, 61, 17, 88, 27, 74, 45, 76, 32, 22, 13, 84, 15, 67, 85, 75, 55, 22, 75, 77, 72, 45, 55, 51, 13, 82, 73, 22, 73, 86, 32, 71, 99, 15, 66, 91, 17, 18, 32, 99, 77, 92, 38, 53, 95, 97, 22, 28, 84, 64, 28, 18, 77, 68, 63, 32, 66, 71, 57, 32, 91, 55, 43, 44, 18, 71, 96, 21, 37, 11, 27, 86, 38, 96, 16, 27, 55, 44, 72, 55, 71, 97, 83, 79, 99, 62, 87, 11, 88, 71, 66, 45, 62, 53, 33, 61, 34, 23, 22, 94, 22, 19, 65, 44, 11, 78, 58, 13, 13, 47, 21, 77, 55, 39, 32, 22, 11, 22, 64, 94, 96, 13, 29, 71, 22, 88, 29, 18, 93, 98, 43, 65, 11, 44, 66, 13, 74, 58, 41, 86, 38, 18, 71, 64, 99, 19, 83, 99, 13, 87, 95, 43, 75, 33, 45, 22, 88, 52, 29, 69, 93, 18, 39, 11, 96, 22, 96, 34, 32, 54, 48, 71, 56, 88, 51, 18, 71, 91, 37, 39, 55, 87, 71, 16, 14, 21, 16, 69, 98, 49, 31, 98, 85, 33, 14, 66, 62, 11, 88, 52, 68, 92, 14, 26, 94, 62, 58, 42, 19, 41, 64, 61, 59, 17, 92, 38, 77, 12, 95, 37, 35, 15, 96, 89, 67, 57, 53, 13, 46, 48, 77, 38, 71, 55, 55, 21, 83, 17, 55, 23, 88, 87, 77, 34, 33, 97, 55, 94, 72, 27, 27, 21, 22, 73, 57, 28, 42, 33, 64, 85, 64, 21, 78, 31, 58, 82, 34, 13, 62, 53, 28, 12, 94, 12, 62, 96, 47, 31, 74, 32, 33, 84, 47, 77, 21, 17, 34, 47, 42, 11, 66, 74, 98, 38, 49, 26, 28, 13, 23, 59, 88, 11, 85, 45, 85, 56, 12, 37, 86, 14, 52, 66, 48, 82, 72, 77, 11, 19, 79, 89, 88, 31, 55, 44, 42, 75, 66, 72, 89, 88, 58, 78, 47, 42, 15, 44, 77, 36, 85, 28, 93, 77, 52, 22, 58, 34, 22, 82, 86, 39, 96, 19, 44, 44, 95, 52, 58, 55, 67, 12, 61, 13, 87, 39, 65, 45, 27, 44, 41, 49, 28, 61, 11, 32, 99, 27, 65, 24, 34, 73, 95, 72, 24, 88, 94, 29, 88, 53, 29, 77, 55, 33, 99, 89, 16, 68, 92, 37, 98, 66, 99, 57, 27, 26, 44, 47, 88, 49, 23, 55, 88, 91, 94, 87, 32, 66, 88, 67, 57, 59, 69, 48, 63, 57, 55, 99, 23, 26, 45, 17, 63, 38, 74, 24, 11, 93, 63, 23, 91, 94, 74, 64, 55, 91, 57, 67, 89, 79, 49, 33, 43, 73, 91, 29, 17, 51, 44, 82, 75, 53, 11, 21, 11, 33, 56, 61, 53, 32, 98, 59, 66, 86, 44, 14, 55, 14, 11, 29, 39, 91, 66, 76, 78, 97, 42, 44, 53, 18, 35, 19, 33, 75, 64, 77, 24, 97, 41, 33, 94, 23, 99, 47, 24, 64, 72, 63, 44, 72, 12, 25, 68, 42, 28, 44, 37, 27, 53, 91, 95, 75, 66, 62, 34, 38, 54, 87, 66, 74, 29, 25, 81, 18, 11, 58, 74, 32, 39, 97, 35, 88, 34, 33, 75, 61, 41, 11, 11, 93, 39, 56, 77, 77, 77, 23, 87, 89, 17, 47, 55, 98, 56, 22, 92, 92, 87, 66, 35, 35, 15, 78, 11, 85, 13, 41, 23, 52, 86, 19, 68, 39, 43, 44, 27, 12, 86, 22, 81, 27, 49, 83, 92, 62, 72, 24, 23, 56, 18, 58, 44, 11, 11, 15, 77, 33, 84, 87, 73, 95, 82, 48, 43, 97, 35, 12, 11, 95, 77, 57, 67, 34, 88, 33, 99, 39, 97, 33, 66, 76, 61, 14, 84, 76, 52, 21, 35, 93, 48, 57, 25, 71, 44, 68, 19, 33, 94, 29, 81, 22, 92, 44, 42, 27, 66, 66, 22, 43, 68, 82, 44, 95, 74, 75, 37, 15, 89, 81, 44, 61, 53, 34, 45, 86, 36, 55, 43, 96, 88, 94, 85, 54, 41, 34, 45, 22, 63, 44, 29, 44, 54, 97, 18, 14, 76, 36, 43, 89, 49, 98, 71, 73, 41, 83, 98, 49, 89, 36, 97, 88, 28, 72, 44, 11, 62, 12, 24, 76, 25, 96, 18, 93, 56, 55, 11, 98, 61, 78, 73, 45, 94, 16, 65, 19, 88, 62, 57, 55, 91, 28, 99, 31, 67, 27, 79, 35, 64, 99, 42, 22, 77, 66, 37, 27, 22, 49, 65, 34, 74, 84, 14, 11, 29, 44, 97, 45, 96, 69, 18, 84, 22, 86, 32, 75, 89, 33, 17, 11, 39, 56, 77, 42, 75, 45, 72, 25, 33, 58, 16, 59, 36, 65, 44, 64, 59, 44, 16, 36, 34, 59, 38, 56, 66, 75, 72, 24, 27, 27, 11, 26, 22, 92, 22, 88, 79, 98, 44, 78, 96, 35, 19, 59, 58, 77, 98, 95, 95, 11, 15, 22, 46, 66, 38, 79, 85, 59, 11, 15, 66, 95, 22, 81, 14, 12, 52, 82, 22, 46, 83, 46, 57, 81, 22, 83, 58, 68, 55, 31, 26, 54, 55, 33, 58, 24, 33, 85, 81, 95, 32, 84, 99, 71, 23, 65, 45, 74, 94, 88, 33, 39, 14, 11, 71, 96, 43, 18, 54, 16, 66, 77, 33, 99, 54, 17, 85, 77, 23, 66, 94, 97, 59, 28, 66, 43, 37, 69, 16, 49, 66, 82, 76, 18, 86, 65, 95, 24, 44, 63, 63, 46, 33, 36, 97, 22, 47, 86, 74, 52, 96, 83, 55, 74, 11, 55, 49, 63, 88, 55, 55, 29, 55, 98, 56, 31, 48, 32, 72, 68, 12, 69, 87, 96, 49, 25, 33, 51, 91, 53, 41, 34, 37, 55, 45, 81, 48, 11, 77, 44, 43, 69, 94, 67, 99, 58, 86, 78, 72, 88, 46, 55, 28, 66, 89, 51, 42, 65, 47, 32, 57, 43, 72, 87, 87, 29]