import multiprocessing
import os
from multiprocessing import freeze_support


def read_input() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


def mix(secret: int, value: int) -> int:
    return secret ^ value


def prune(secret: int) -> int:
    return secret % 16777216


def generate_next_secret(secret: int) -> int:
    result = mix(secret, secret * 64)
    result = prune(result)
    result = mix(result, result // 32)
    result = prune(result)
    result = mix(result, result * 2048)
    result = prune(result)
    return result


def generate_prices(initial: int, count: int) -> list[int]:
    prices = []
    current = initial

    prices.append(current % 10)

    for _ in range(count):
        current = generate_next_secret(current)
        prices.append(current % 10)

    return prices


def get_price_changes(prices: list[int]) -> list[int]:
    """Calculate changes between consecutive prices"""
    return [b - a for a, b in zip(prices[:-1], prices[1:])]


def find_sequence_value(changes: list[int], sequence: tuple[int], prices: list[int]) -> int:
    """Find the price when sequence first appears, or 0 if not found"""
    for i in range(len(changes) - len(sequence) + 1):
        if tuple(changes[i:i + len(sequence)]) == sequence:
            return prices[i + len(sequence)]  # Price after sequence completes
    return 0


def evaluate_sequence(sequence: tuple[int], initial_secrets: list[int]) -> int:
    total_bananas = 0

    for initial in initial_secrets:
        prices = generate_prices(initial, 2000)
        changes = get_price_changes(prices)

        value = find_sequence_value(changes, sequence, prices)
        total_bananas += value

    return total_bananas


def evaluate_sequence_parallel(args):
    sequence, initial_secrets = args
    return sequence, evaluate_sequence(sequence, initial_secrets)


def find_best_sequence(initial_secrets: list[int]) -> tuple[tuple[int], int]:
    all_sequences = [(a, b, c, d)
                     for a in range(-9, 10)
                     for b in range(-9, 10)
                     for c in range(-9, 10)
                     for d in range(-9, 10)]

    with multiprocessing.Pool() as pool:
        results = pool.map(evaluate_sequence_parallel, [(seq, initial_secrets) for seq in all_sequences])
    best_sequence, max_bananas = max(results, key=lambda x: x[1])

    return best_sequence, max_bananas


if __name__ == "__main__":
    freeze_support()

    lines = read_input()
    inputs = [int(line) for line in lines]

    sequence, bananas = find_best_sequence(inputs)
    print(f"best sequence: {sequence}")
    print(f"total bananas: {bananas}")
