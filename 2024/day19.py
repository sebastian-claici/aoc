from functools import cache
import re

from aocd.models import Puzzle


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


puzzle = Puzzle(year=2024, day=19)
data = puzzle.input_data

patterns, flags = data.split("\n\n")
patterns = patterns.strip().split(", ")

flags = [line.strip() for line in flags.split("\n")]


@cache
def count_matches(s):
    if s == "":
        return 1

    ans = 0
    for pat in patterns:
        if s.startswith(pat):
            ans += count_matches(s[len(pat):])

    return ans


p1_ans = 0
p2_ans = 0
for flag in flags:
    cnt = count_matches(flag)
    p1_ans += (cnt > 0)
    p2_ans += cnt

print(p1_ans)
print(p2_ans)
