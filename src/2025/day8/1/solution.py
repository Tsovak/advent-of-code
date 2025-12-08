import os
from math import sqrt 
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        self.parent[root_x] = root_y
        
        return True



def read_lines() -> list[str]:
    filename = os.path.join(ROOT_DIR, 'data.txt')

    with open(filename, "rb") as f:
        lines = f.read().splitlines()

    return lines

def distance(p1, p2):
    return sqrt(
        (p1[0] - p2[0]) ** 2 + 
        (p1[1] - p2[1]) ** 2 + 
        (p1[2] - p2[2]) ** 2
    )

def calculate_edges(points: set[tuple[int, int, int]]) -> list[tuple[float, tuple[int, int, int], tuple[int, int, int]]]:
    edges = []
    points = list(points)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            edges.append((d, points[i], points[j]))
    
    edges.sort()
    return edges
            

lines = read_lines()

dataset = set()

dataset = set()
for line in lines:
    line = line.decode("utf-8")
    x, y, z = map(int, line.split(","))
    dataset.add((x, y, z))


edges = calculate_edges(dataset)
# print(edges)

uf = UnionFind()
pairs_processed = 0

for dist, p1, p2 in edges:
    uf.union(p1, p2)
    pairs_processed += 1

    if pairs_processed == 1000:
        break

from collections import Counter
roots = [uf.find(p) for p in dataset]
circuit_sizes = sorted(Counter(roots).values(), reverse=True)

print("circuit sizes:", circuit_sizes[:3])
print("result:", circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2])