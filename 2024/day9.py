import itertools
import re
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import lru_cache
from math import gcd, lcm

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=9)
data = puzzle.input_data

bits = []
chunks = []
space = []
blocks = []
idx = 0
for i in range(0, len(data), 2):
    n = int(data[i])
    chunks.append((len(blocks), idx, n))
    for _ in range(n):
        bits.append((len(blocks), idx, 1))
        blocks.append(idx)
    idx += 1
    if i + 1 < len(data):
        s = int(data[i + 1])
        space.append((len(blocks), s))
        for _ in range(s):
            blocks.append(None)


space_p1 = deepcopy(space)
blocks_p1 = deepcopy(blocks)
for pos, idx, s in reversed(bits):
    for i, (st, sz) in enumerate(space_p1):
        if st < pos and s <= sz:
            for k in range(min(s, sz)):
                blocks_p1[st + k] = idx
                blocks_p1[pos + k] = None
            space_p1[i] = (st + s, max(0, sz - s))
            break

print(sum(i * x for i, x in enumerate(blocks_p1) if x is not None))

for pos, idx, s in reversed(chunks):
    for i, (st, sz) in enumerate(space):
        if st < pos and s <= sz:
            for k in range(s):
                blocks[st + k] = idx
                blocks[pos + k] = None
            space[i] = (st + s, sz - s)
            break

print(sum(i * x for i, x in enumerate(blocks) if x is not None))
