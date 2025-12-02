import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.readlines()

    return lines

def find_invalid_ranges(start:str, end:str) -> list[int] :
    start = int(start)
    end = int(end)
    if start >= end:
        return []

    def is_repeated(n:int) -> bool:
        s = str(n)
        length = len(s)
        for i in range(0, length // 2):
            res = [s[k : k + i+1] for k in range(0, length, i+1)]
            sets = set(res)
            if len(sets) == 1:
                return True

        return False

    total = [ i for i in range(start, end+1) if is_repeated(i) ]
    return total

lines = read_lines()

line = lines[0].decode("utf-8")
ranges = line.split(",")
sums = 0
for r in ranges:
    start, end = r.split("-")
    sums += sum(find_invalid_ranges(start, end))

print(sums)