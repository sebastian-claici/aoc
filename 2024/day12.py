import itertools
import re
from collections import Counter, defaultdict, deque
from functools import cache
from math import gcd, lcm

import numpy as np

from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=12)
data = puzzle.input_data


grid = [[c for c in line.strip()] for line in data.split("\n")]
n, m = len(grid), len(grid[0])

visited = set()
adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(node, plants):
    visited.add(node)
    plants.append(node)

    x, y = node
    for dx, dy in adj:
        if not (0 <= x + dx < n and 0 <= y + dy < m):
            continue
        if (x + dx, y + dy) in visited:
            continue
        if grid[x + dx][y + dy] != grid[x][y]:
            continue
        dfs((x + dx, y + dy), plants)


visited = set()
p1_soln = 0
p2_soln = 0
for x in range(n):
    for y in range(m):
        if (x, y) in visited:
            continue
        plants = []
        dfs((x, y), plants)
        area = len(plants)
        boundaries = []
        for (nx, ny) in plants:
            for dx, dy in adj:
                if not (0 <= nx + dx < n and 0 <= ny + dy < m) or grid[nx + dx][ny + dy] != grid[nx][ny]:
                    boundaries.append((nx + dx + (ny + dy) * 1j, dx + dy * 1j))
        perim = len(boundaries)
        p1_soln += area * perim

        sides = 0
        while boundaries:
            sides += 1
            pos, d = boundaries.pop()
            for next_d in [d * 1j, -d * 1j]:
                k = 1
                while (pos + k * next_d, d) in boundaries:
                    boundaries.remove((pos + k * next_d, d))
                    k += 1
        p2_soln += area * sides

print(p1_soln)
print(p2_soln)
