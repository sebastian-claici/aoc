import itertools
import re
from collections import Counter, defaultdict
from functools import lru_cache
from math import gcd, lcm

from aocd.models import Puzzle


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


puzzle = Puzzle(year=2024, day=5)
data = puzzle.input_data


def split_pages(data):
    after = defaultdict(set)
    order, pages = data.split("\n\n")
    for line in order.split("\n"):
        x, y = ints(line)
        after[x].add(y)

    good_pages, bad_pages = [], []
    for line in pages.split("\n"):
        nums = ints(line)
        good = True
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] in after[num]:
                    good = False
        if good:
            good_pages.append(nums)
        else:
            bad_pages.append(nums)

    return after, good_pages, bad_pages


def p1(data):
    _, pages, _ = split_pages(data)
    soln = sum(p[len(p) // 2] for p in pages)
    return str(soln)


def fix(nums, order):
    for i, num in enumerate(nums):
        for j in range(i):
            if nums[j] in order[num]:
                nums[i], nums[j] = nums[j], nums[i]
                return fix(nums, order)

    return nums[len(nums) // 2]


def p2(data):
    after, _, pages = split_pages(data)
    soln = sum(fix(page, after) for page in pages)
    return str(soln)


p1_s = p1(data)
p2_s = p2(data)
print(p1_s)
print(p2_s)
if p1_s != "":
    puzzle.answer_a = p1_s
if p2_s != "":
    puzzle.answer_b = p2_s
