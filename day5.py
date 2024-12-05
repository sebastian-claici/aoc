import itertools
import re
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import gcd, lcm

from aocd.models import Puzzle


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


puzzle = Puzzle(year=2024, day=5)
data = puzzle.input_data


def split_pages(data):
    si = defaultdict(set)
    pi = defaultdict(set)
    order, pages = data.split("\n\n")
    for line in order.split("\n"):
        x, y = ints(line)
        si[x].add(y)
        pi[y].add(x)

    good_pages, bad_pages = [], []
    for line in pages.split("\n"):
        nums = ints(line)
        good = True
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] in si[num]:
                    good = False
        if good:
            good_pages.append(nums)
        else:
            bad_pages.append(nums)

    return pi, si, good_pages, bad_pages


def p1(data):
    _, _, pages, _ = split_pages(data)
    soln = sum(p[len(p) // 2] for p in pages)
    return str(soln)


def topo_sort(nums, parent, child):
    nums = set(nums)

    q = deque([])
    degree = {}
    for num in nums:
        degree[num] = len(parent[num] & nums)
        if degree[num] == 0:
            q.append(num)

    result = []
    while q:
        num = q.popleft()
        result.append(num)
        for c in child[num] & nums:
            degree[c] -= 1
            if degree[c] == 0:
                q.append(c)

    return result[len(result) // 2]


def p2(data):
    pi, si, _, pages = split_pages(data)

    soln = sum(topo_sort(page, pi, si) for page in pages)
    return str(soln)


p1_s = p1(data)
p2_s = p2(data)
print(p1_s)
print(p2_s)
if p1_s != "":
    puzzle.answer_a = p1_s
if p2_s != "":
    puzzle.answer_b = p2_s
