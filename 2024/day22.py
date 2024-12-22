import re
import sys
from collections import defaultdict, deque
from functools import cache

from aocd.models import Puzzle

sys.setrecursionlimit(1000000)


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


puzzle = Puzzle(year=2024, day=22)
data = puzzle.input_data

mod = 16777216


def simulate(number):
    number = ((number * 64) ^ number) % mod
    number = ((number // 32) ^ number) % mod
    number = ((number * 2048) ^ number) % mod

    return number


patterns = defaultdict(list)

ans = 0
for line in data.split("\n"):
    number = int(line.strip())

    best = defaultdict(int)
    diffs = deque([])
    digit = number % 10
    for _ in range(2000):
        number = simulate(number)
        diffs.append((number % 10) - digit)
        digit = number % 10
        if len(diffs) == 4:
            if tuple(diffs) not in best:
                best[tuple(diffs)] = digit
            diffs.popleft()

    for pat, val in best.items():
        patterns[pat].append(val)

    ans += number

print(ans)

best = 0
for pat, values in patterns.items():
    best = max(best, sum(values))
print(best)
