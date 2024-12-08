import itertools
import re
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import gcd, lcm

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=8)
data = puzzle.input_data
grid = [[c for c in line.strip()] for line in data.split("\n")]

n, m = len(grid), len(grid[0])
positions = defaultdict(list)
for i in range(n):
    for j in range(m):
        if grid[i][j].isalnum():
            positions[grid[i][j]].append(complex(i, j))


antinodes = set()
for c, pos in positions.items():
    for i, p in enumerate(pos):
        for j, q in enumerate(pos[i + 1 :]):
            dr = q - p
            for dir in (dr, -dr):
                pm = p
                while 0 <= pm.real < n and 0 <= pm.imag < m:
                    antinodes.add(pm)
                    pm += dir

print(len(antinodes))
