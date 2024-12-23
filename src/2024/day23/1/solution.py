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


def find_triplets(graph: dict[str, set[str]], filter_prefix: str = None) -> list[set[str]]:
    triplets = []
    nodes = list(graph.keys())

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            for k in range(j + 1, len(nodes)):
                a, b, c = nodes[i], nodes[j], nodes[k]
                if b in graph[a] and c in graph[a] and c in graph[b]:
                    triplet = {a, b, c}
                    if filter_prefix is None or any(node.startswith(filter_prefix) for node in triplet):
                        triplets.append(triplet)

    return triplets


lines = read_input()

graph = build_graph(lines)

all_triplets = find_triplets(graph)
print(f"total triplets: {len(all_triplets)}\n")

t_triplets = find_triplets(graph, 't')
print(f"triplets with prefix: {len(t_triplets)}")
for triplet in sorted(t_triplets):
    print(','.join(sorted(triplet)))
