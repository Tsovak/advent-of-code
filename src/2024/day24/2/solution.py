import os


def read_input() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


lines = [l.split() for l in read_input() if '->' in l]


def right(z: str, op: str) -> bool:
    return any(
        op == exp and z in (a, b)
        for a, exp, b, _, _ in lines
    )


result = []
for a, op, b, _, z in lines:
    if (
            op == "XOR" and all(d[0] not in 'xyz' for d in (a, b, z)) or
            op == "AND" and not "x00" in (a, b) and right(z, 'XOR') or
            op == "XOR" and not "x00" in (a, b) and right(z, 'OR') or
            op != "XOR" and z[0] == 'z' and z != "z45"
    ):
        result.append(z)

result = sorted(result)
print(",".join(result))
