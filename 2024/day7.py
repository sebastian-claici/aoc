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
    return ""


def p2(data):
    return ""


p1_s = p1(data)
p2_s = p2(data)
if p1_s != "":
    print(p1_s)
    puzzle.answer_a = p1_s
if p2_s != "":
    print(p2_s)
    puzzle.answer_b = p2_s
