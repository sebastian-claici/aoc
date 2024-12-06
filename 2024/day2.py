import re
from collections import Counter, defaultdict
from functools import lru_cache
from math import gcd, lcm

from aocd import get_data, submit

data = get_data(day=2, year=2024)
lines = data.split("\n")


def is_safe(nums):
    inc = all(1 <= y - x <= 3 for x, y in zip(nums, nums[1:]))
    dec = all(1 <= x - y <= 3 for x, y in zip(nums, nums[1:]))
    return inc or dec


def p1(lines):
    nums = list(map(ints, lines))
    return len(list(filter(is_safe, nums)))


def p2(lines):
    nums = map(ints, lines)
    soln = 0
    for n in nums:
        if any(is_safe(n[:i] + n[i + 1 :]) for i in range(len(n))):
            soln += 1
    return soln


print(p1(lines))
print(p2(lines))
