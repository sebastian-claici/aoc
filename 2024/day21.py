import re
import sys
from collections import defaultdict, deque
from functools import cache

from aocd.models import Puzzle

sys.setrecursionlimit(1000000)


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


puzzle = Puzzle(year=2024, day=21)
data = puzzle.input_data

directional = [[None, "^", "A"], ["<", "v", ">"]]
numeric = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]

dir_pos = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}
num_pos = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (1, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}
adj_to_dir = {(0, 1): ">", (0, -1): "<", (1, 0): "v", (-1, 0): "^"}


def bfs(grid, sx, sy):
    adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n, m = len(grid), len(grid[0])

    dist = defaultdict(lambda: float("inf"))
    prev = defaultdict(list)

    prev[(sx, sy)] = [(-1, -1, -1)]
    dist[(sx, sy)] = 0
    q = deque([(0, (sx, sy))])
    while q:
        d, (x, y) = q.popleft()
        for dx, dy in adj:
            if not (0 <= x + dx < n and 0 <= y + dy < m):
                continue

            nx, ny = x + dx, y + dy
            if grid[nx][ny] == None:
                continue

            if dist[(nx, ny)] == d + 1:
                prev[(nx, ny)].append((x, y, adj_to_dir[(dx, dy)]))
            if dist[(nx, ny)] > d + 1:
                dist[(nx, ny)] = d + 1
                prev[(nx, ny)] = [(x, y, adj_to_dir[(dx, dy)])]
                q.append((d + 1, (nx, ny)))

    return dist, prev


def find_paths(paths, path, prev, x, y):
    if prev[(x, y)] == [(-1, -1, -1)]:
        curr_path = "A" + "".join(path[::-1]) + "A"
        paths.append(curr_path)

    for px, py, dir in prev[(x, y)]:
        path.append(dir)
        find_paths(paths, path, prev, px, py)
        path.pop()


num_robots = 26


@cache
def count_moves(sx, sy, ex, ey, robot):
    if robot == 0:
        return 1

    grid = numeric if robot == num_robots else directional
    _, prev = bfs(grid, sx, sy)

    paths, path = [], []
    find_paths(paths, path, prev, ex, ey)

    best = float("inf")
    for path in paths:
        path_cost = 0
        for c1, c2 in zip(path, path[1:]):
            (ir, ic), (jr, jc) = dir_pos[c1], dir_pos[c2]
            path_cost += count_moves(ir, ic, jr, jc, robot - 1)
        best = min(best, path_cost)

    return best


def solve(data):
    lines = [line.strip() for line in data.split("\n")]
    soln = 0
    for line in lines:
        line = "A" + line
        moves = 0
        for c1, c2 in zip(line, line[1:]):
            (ir, ic), (jr, jc) = num_pos[c1], num_pos[c2]
            moves += count_moves(ir, ic, jr, jc, num_robots)
        num = int("".join(c for c in line if c.isdigit()))
        soln += num * moves

    return soln


print(solve(data))
