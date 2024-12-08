import itertools
import re
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import gcd, lcm

import numpy as np
from aocd.models import Puzzle

adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(grid, sx, sy, ex, ey):
    n, m = len(grid), len(grid[0])
    dist = 1_000_000 * np.ones((n, m), dtype=np.int32)

    q = deque([(0, (sx, sy))])
    while q:
        d, (x, y) = q.pop()
        for dx, dy in adj:
            if not (0 <= x + dx < n and 0 <= y + dy < m):
                continue
            if ord(grid[x][y]) - ord(grid[x + dx][y + dy]) > 1:
                continue
            if d + 1 < dist[x + dx][y + dy]:
                dist[x + dx][y + dy] = d + 1
                q.append((d + 1, (x + dx, y + dy)))

    return dist[(ex, ey)]


puzzle = Puzzle(year=2024, day=9)
data = puzzle.input_data
