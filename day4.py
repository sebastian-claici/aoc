import itertools
import re
from collections import Counter, defaultdict
from functools import lru_cache
from math import gcd, lcm

from aocd.models import Puzzle


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


puzzle = Puzzle(year=2024, day=4)
data = puzzle.input_data.split("\n")

adj = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0)]


def find(x, y, grid, word):
    ans = 0
    for dx, dy in adj:
        xys = [(x, y)]
        for k in range(1, len(word)):
            nx, ny = xys[-1]
            nx += dx
            ny += dy
            if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                break
            if grid[nx][ny] != word[k]:
                break
            xys.append((nx, ny))
        else:
            ans += 1

    return ans


def find_mas(x, y, grid):
    if not (
        0 <= (x - 1) and (x + 1) < len(grid) and 0 <= (y - 1) and (y + 1) < len(grid)
    ):
        return 0

    d1, d2 = False, False
    if (grid[x - 1][y - 1] == "M" and grid[x + 1][y + 1] == "S") or (
        grid[x - 1][y - 1] == "S" and grid[x + 1][y + 1] == "M"
    ):
        d1 = True
    if (grid[x - 1][y + 1] == "M" and grid[x + 1][y - 1] == "S") or (
        grid[x + 1][y - 1] == "M" and grid[x - 1][y + 1] == "S"
    ):
        d2 = True

    return int(d1 and d2)


def p1(data):
    count = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == "X":
                ans = find(x, y, data, "XMAS")
                count += ans
    return str(count)


def p2(data):
    count = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == "A":
                ans = find_mas(x, y, data)
                count += ans
    return str(count)


p1_s = p1(data)
p2_s = p2(data)
if p1_s != "":
    puzzle.answer_a = p1_s
if p2_s != "":
    puzzle.answer_b = p2_s
