import os


def read_input() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


def mix(secret: int, value: int) -> int:
    return secret ^ value


def prune(secret: int) -> int:
    return secret % 16777216


def generate_next_secret(secret: int) -> int:
    # step 1: multiply by 64, mix, and prune
    result = mix(secret, secret * 64)
    result = prune(result)

    # step 2: divide by 32 (floor division), mix, and prune
    result = mix(result, result // 32)
    result = prune(result)

    # step 3: multiply by 2048, mix, and prune
    result = mix(result, result * 2048)
    result = prune(result)

    return result


def generate_nth_secret(initial_secret: int, n: int) -> int:
    current = initial_secret
    for _ in range(n):
        current = generate_next_secret(current)
    return current


lines = read_input()

inputs = [int(line) for line in lines]
result = sum([generate_nth_secret(initial, 2000) for initial in inputs])
print(result)
