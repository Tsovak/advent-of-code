import os
from collections import defaultdict


def read_input() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


def build_gates_connections(lines: list[str]) -> tuple[dict[str, bool], dict[str, set[str]]]:
    separator_index = lines.index('')
    gate_lines = lines[:separator_index]
    connection_lines = lines[separator_index + 1:]

    gates: dict[str, bool] = {}

    for g in gate_lines:
        sp = g.split(": ")
        gates[sp[0]] = sp[1] == "1"

    connections = defaultdict(set)
    for line in connection_lines:
        a, b = line.split(' -> ')
        connections[a].add(b)
    return gates, connections


def operate(a: bool, b: bool, op: str) -> bool:
    if op == "AND":
        return a and b
    elif op == "OR":
        return a or b
    elif op == "XOR":
        return a ^ b
    else:
        raise ValueError(f"Unknown operation: {op}")


def solve(gates: dict[str, bool], connections: dict[str, set[str]]) -> dict[str, bool]:
    if len(connections) == 0:
        return gates

    connections_copy = connections.copy()
    for k, v in connections_copy.items():
        if len(k) == 3:
            continue

        first, op, second = k.split(" ")
        if first in gates and second in gates:
            value = operate(gates[first], gates[second], op)
            for item in v:
                gates[item] = value
            del connections[k]

    return solve(gates, connections)


def get_decimal_number(all_gates: dict[str, bool]) -> int:
    z_gates = {k: v for k, v in all_gates.items() if k.startswith("z")}
    z_gates = sorted(z_gates.items(), key=lambda x: x[0])
    return sum(2 ** i for i, (k, v) in enumerate(z_gates) if v)


lines = read_input()
gates, connections = build_gates_connections(lines)
gates = solve(gates, connections)
print(get_decimal_number(gates))
