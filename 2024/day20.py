from itertools import combinations
from collections import defaultdict
from copy import deepcopy
import re
from collections import deque

from aocd.models import Puzzle


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


puzzle = Puzzle(year=2024, day=20)
data = puzzle.input_data

grid = [[c for c in line.strip()] for line in data.split("\n")]
n, m = len(grid), len(grid[0])

sx, sy = 0, 0
blocked = []
for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c == 'S':
            sx, sy = i, j
        if c == '#':
            blocked.append((i, j))

def bfs(grid, sx, sy):
    adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque([(0, sx, sy)])
    dists = {(sx, sy): 0}
    while q:
        d, x, y = q.popleft()

        for dx, dy in adj:
            if not (0 <= x + dx < n and 0 <= y + dy < m):
                continue
            if grid[x + dx][y + dy] == "#":
                continue
            if (x + dx, y + dy) in dists:
                continue
            dists[(x + dx, y + dy)] = d + 1
            q.append((d + 1, x + dx, y + dy))
    return dists


p1_ans = 0
p2_ans = 0
dists = bfs(grid, sx, sy)
for ((px, py), dp), ((qx, qy), dq) in combinations(dists.items(), 2):
    manh = abs(px - qx) + abs(py - qy)
    if dq - dp - manh >= 100:
        p1_ans += (manh == 2)
        p2_ans += (manh < 21)

print(p1_ans)
print(p2_ans)
