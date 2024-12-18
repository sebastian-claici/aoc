from copy import deepcopy
import re
from collections import deque

from aocd.models import Puzzle


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


puzzle = Puzzle(year=2024, day=18)
data = puzzle.input_data

n = 71
grid = [['.' for _ in range(n)] for _ in range(n)]

def bfs(grid):
    adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque([(0, 0, 0)])
    seen = set()
    while q:
        d, y, x = q.popleft()
        if (y, x) in seen:
            continue
        if (y, x) == (n - 1, n - 1):
            return d
        seen.add((y, x))
        for dy, dx in adj:
            if not (0 <= x + dx < n and 0 <= y + dy < n):
                continue
            if grid[y + dy][x + dx] == '#':
                continue
            q.append((d + 1, y + dy, x + dx))
    return None

lo, hi = 0, len(data.split("\n"))
while lo < hi:
    mid = (lo + hi) // 2
    grid_c = deepcopy(grid)

    for i, line in enumerate(data.split("\n")):
        if i > mid:
            break
        x, y = ints(line)
        grid_c[y][x] = '#'

    dist = bfs(grid_c)
    if dist is None:
        hi = mid
    else:
        lo = mid + 1
print(data.split("\n")[lo])
