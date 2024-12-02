import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    lines = [line.decode("utf-8").strip() for line in lines]
    return lines


lines = read_lines()


def is_sequence_safe(sequence):
    is_increasing = all(sequence[i] < sequence[i + 1] for i in range(len(sequence) - 1))
    is_decreasing = all(sequence[i] > sequence[i + 1] for i in range(len(sequence) - 1))

    if not (is_increasing or is_decreasing):
        return False

    for i in range(len(sequence) - 1):
        diff = abs(sequence[i] - sequence[i + 1])
        if diff < 1 or diff > 3:
            return False

    return True


def is_report_safe(report):
    levels = [int(x) for x in report.split()]

    if is_sequence_safe(levels):
        return True

    for i in range(len(levels)):
        test_levels = levels[:i] + levels[i + 1:]

        if is_sequence_safe(test_levels):
            return True

    return False


safe_reports = sum(1 for line in lines if is_report_safe(line))
print(safe_reports) # 271
