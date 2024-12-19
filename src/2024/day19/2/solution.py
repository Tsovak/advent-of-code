import os


def read_input() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


# working slowly
def all_possible_variants_slow(patterns: list[str], design: str) -> int:
    if not design:
        return 1

    result = 0
    for pattern in patterns:
        if design.startswith(pattern):
            result += all_possible_variants_slow(patterns, design[len(pattern):])

    return result


def all_possible_variants_optimized(patterns: list[str], designs: list[str]) -> int:
    def count_variants(design: str) -> int:
        if not design:
            return 1

        result = 0
        for pattern in patterns:
            if design.startswith(pattern):
                result += count_variants(design[len(pattern):])

        return result

    return sum(count_variants(d) for d in designs)


# alternative implementation using bottom-up DP
def all_possible_variants_dp(patterns: list[str], designs: list[str]) -> int:
    def count_variants_for_design(design: str) -> int:
        n = len(design)
        # dp[i] represents number of ways to build string ending at position i
        dp = [0] * (n + 1)
        dp[0] = 1  # an empty string has one way

        for i in range(n):
            if dp[i] == 0:
                continue

            for pattern in patterns:
                if design[i:].startswith(pattern):
                    next_pos = i + len(pattern)
                    if next_pos <= n:
                        dp[next_pos] += dp[i]

        return dp[n]

    return sum(count_variants_for_design(design) for design in designs)


lines = read_input()
patterns = lines[0].split(", ")
design = lines[2:]

result = all_possible_variants_dp(patterns, design)
print(result)
