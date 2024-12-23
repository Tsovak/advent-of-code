import os
from collections import defaultdict


def read_input() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


def build_graph(lines: list[str]) -> dict[str, set[str]]:
    graph = defaultdict(set)
    for line in lines:
        a, b = line.split('-')
        graph[a].add(b)
        graph[b].add(a)
    return graph


def is_subgraph(graph, vertices):
    return all(
        v2 in graph[v1]
        for v1 in vertices
        for v2 in vertices
        if v1 != v2
    )


def find_max_subgraph_slowest(graph):
    nodes = list(graph.keys())
    n = len(nodes)

    # start with largest possible size
    for size in range(n, 1, -1):
        def check_combination(combo, start):
            if len(combo) == size:
                if is_subgraph(graph, combo):
                    return combo
                return None

            for i in range(start, n):
                node = nodes[i]
                if all(node in graph[v] for v in combo):
                    result = check_combination(combo | {node}, i + 1)
                    if result:
                        return result
            return None

        result = check_combination(set(), 0)
        if result:
            return result

    return None


def find_max_subgraph(graph):
    def bron_kerbosch(r, p, x, max_subgraph):
        if len(p) == 0 and len(x) == 0:
            if len(r) > len(max_subgraph[0]):
                max_subgraph[0] = r.copy()
            return

        max_node = max(p | x, key=lambda u: len(p & graph[u]), default=None)
        if max_node is None:
            return

        for v in p - graph[max_node]:
            bron_kerbosch(
                r | {v},
                p & graph[v],
                x & graph[v],
                max_subgraph
            )
            p = p - {v}
            x = x | {v}

    max_subgraph = [set()]
    bron_kerbosch(set(), set(graph.keys()), set(), max_subgraph)
    return max_subgraph[0]


lines = read_input()
graph = build_graph(lines)
max_subgraph = find_max_subgraph(graph)

if max_subgraph:
    password = ','.join(sorted(max_subgraph))
    print(f"password: {password}")
