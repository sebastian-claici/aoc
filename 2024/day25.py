import sys
from collections import defaultdict, Counter, deque
import networkx as nx

from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=25)
data = puzzle.input_data

elems = data.split("\n\n")

def get_counts(lines):
    n, m = len(lines), len(lines[0])
    counts = []
    for j in range(m):
        count = 0
        for i in range(n):
            count += (lines[i][j] == '#')
        counts.append(count - 1)

    return counts

keys = []
locks = []
for elem in elems:
    lines = [line.strip() for line in elem.splitlines()]
    if all(c == '#' for c in lines[0]):
        keys.append(get_counts(lines))
    elif all(c == '#' for c in lines[-1]):
        locks.append(get_counts(lines))

ans = 0
for key in keys:
    for lock in locks:
        for i in range(len(key)):
            if key[i] + lock[i] > 5:
                break
        else:
            ans += 1
print(ans)
