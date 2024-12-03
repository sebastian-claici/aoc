from collections import Counter, defaultdict
from functools import lru_cache
from math import gcd, lcm

from aocd import get_data, submit

data = get_data(day=2, year=2024)
lines = data.split("\n")


def is_safe(nums):
    inc = True
    for x, y in zip(nums, nums[1:]):
        if not (y >= x and 1 <= (y - x) <= 3):
            inc = False
    dec = True
    for x, y in zip(nums, nums[1:]):
        if not (y <= x and 1 <= (x - y) <= 3):
            dec = False
    return inc or dec


soln = 0
for line in lines:
    nums = [int(c) for c in line.split()]
    if is_safe(nums):
        soln += 1
    else:
        for i in range(0, len(nums)):
            nums_tmp = nums[:i] + nums[i + 1 :]
            if is_safe(nums_tmp):
                soln += 1
                break

# submit(str(soln))

# submit(str(soln))
