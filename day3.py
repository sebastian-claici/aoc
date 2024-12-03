import re
from collections import Counter, defaultdict
from functools import lru_cache
from math import gcd, lcm

from aocd import get_data, submit

data = get_data(day=3, year=2024)
soln = 0
good = True
for m in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", data):
    if m.group() == "do()":
        good = True
    elif m.group() == "don't()":
        good = False
    if good and m.group().startswith("mul"):
        soln += int(m.group(1)) * int(m.group(2))
print(soln)
