from collections import deque

from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=10)
data = puzzle.input_data


grid = [[int(c) for c in line.strip()] for line in data.split("\n")]

n, m = len(grid), len(grid[0])
starts = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            starts.append((i, j))

adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]

soln_p1 = 0
soln_p2 = 0
for sx, sy in starts:
    visited = set([])
    distinct = 0
    q = deque([(sx, sy)])
    while q:
        x, y = q.pop()
        if grid[x][y] == 9:
            visited.add((x, y))
            distinct += 1
        for dx, dy in adj:
            if not (0 <= x + dx < n and 0 <= y + dy < m):
                continue
            if grid[x + dx][y + dy] != grid[x][y] + 1:
                continue
            q.append((x + dx, y + dy))

    soln_p1 += len(visited)
    soln_p2 += distinct

print(soln_p1)
print(soln_p2)
