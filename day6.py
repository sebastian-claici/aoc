import itertools
import re
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import gcd, lcm

from aocd.models import Puzzle


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


puzzle = Puzzle(year=2024, day=6)
data = puzzle.input_data

adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_start(grid):
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "^":
                return i, j

    return None


def p1(data):
    grid = data.split("\n")
    sx, sy = get_start(grid)

    visited = set([])
    idx = 0
    q = deque([(sx, sy, idx)])
    while q:
        x, y, idx = q.popleft()
        dx, dy = adj[idx]
        visited.add((x, y))
        if not (0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0])):
            break
        if grid[x + dx][y + dy] == "#":
            idx = (idx + 1) % len(adj)
            q.append((x, y, idx))
        else:
            q.append((x + dx, y + dy, idx))

    return str(len(visited))


def p2(data):
    grid = data.split("\n")
    sx, sy = get_start(grid)

    soln = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == sx and j == sy:
                continue
            if grid[i][j] == "#":
                continue

            visited = set([])
            idx = 0
            q = deque([(sx, sy, idx)])
            while q:
                x, y, idx = q.popleft()
                dx, dy = adj[idx]
                if (x, y, idx) in visited:
                    soln += 1
                    break
                visited.add((x, y, idx))
                if not (0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0])):
                    break
                if grid[x + dx][y + dy] == "#" or (x + dx == i and y + dy == j):
                    idx = (idx + 1) % len(adj)
                    q.append((x, y, idx))
                else:
                    q.append((x + dx, y + dy, idx))

    return str(soln)


p1_s = p1(data)
p2_s = p2(data)
if p1_s != "":
    print(p1_s)
    puzzle.answer_a = p1_s
if p2_s != "":
    print(p2_s)
    puzzle.answer_b = p2_s
