from collections import deque, defaultdict
from heapq import heappush, heappop

from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=16)
data = puzzle.input_data

grid = [[c for c in line.strip()] for line in data.split("\n")]

sx, sy = 0, 0
ex, ey = 0, 0
for x, line in enumerate(grid):
    for y, c in enumerate(line):
        if c == 'S':
            sx, sy = x, y
        elif c == 'E':
            ex, ey = x, y


def dijkstra(grid, sx, sy):
    n, m = len(grid), len(grid[0])

    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(list)
    dist[(sx, sy, 0, 1)] = 0
    q = [(0, (sx, sy, 0, 1))]
    while q:
        d, (px, py, dx, dy) = heappop(q)
        dir = dx + dy * 1j
        new_dirs = [dir * 1j, -dir * 1j]
        for new_dir in new_dirs:
            ndx, ndy = int(new_dir.real), int(new_dir.imag)

            if dist[(px, py, ndx, ndy)] == d + 1000:
                prev[(px, py, ndx, ndy)].append((px, py, dx, dy))

            if dist[(px, py, ndx, ndy)] > d + 1000:
                dist[(px, py, ndx, ndy)] = d + 1000
                prev[(px, py, ndx, ndy)] = [(px, py, dx, dy)]
                heappush(q, (d + 1000, (px, py, ndx, ndy)))

        npx, npy = px + dx, py + dy
        if not (0 <= npx < n and 0 <= npy < m):
            continue
        if grid[npx][npy] == '#':
            continue

        if dist[(npx, npy, dx, dy)] == d + 1:
            prev[(npx, npy, dx, dy)].append((px, py, dx, dy))

        if dist[(npx, npy, dx, dy)] > d + 1:
            prev[(npx, npy, dx, dy)] = [(px, py, dx, dy)]
            dist[(npx, npy, dx, dy)] = d + 1
            heappush(q, (d + 1, (npx, npy, dx, dy)))

    return dist, prev


dist, prev = dijkstra(grid, sx, sy)

soln = float("inf")
for pd, d in dist.items():
    px, py, _, _ = pd
    if px == ex and py == ey:
        soln = min(soln, d)
print(soln)

end_states = []
for pd, d in dist.items():
    px, py, dx, dy = pd
    if px == ex and py == ey and d == soln:
        end_states.append((px, py, dx, dy))

visited = set()
back_q = deque(end_states)
while back_q:
    px, py, dx, dy = back_q.pop()
    visited.add((px, py))
    for npx, npy, ndx, ndy in prev[(px, py, dx, dy)]:
        back_q.appendleft((npx, npy, ndx, ndy))

print(len(visited))
