from collections import Counter

from aocd import data

lines = data.split("\n")
xs = []
ys = []
for line in lines:
    nums = [int(x) for x in line.split()]
    xs.append(nums[0])
    ys.append(nums[1])


def p1(xs, ys):
    xs = sorted(xs)
    ys = sorted(ys)

    soln = 0
    for x, y in zip(xs, ys):
        soln += abs(x - y)
    return soln


def p2(xs, ys):
    counter = Counter(ys)
    soln = 0
    for x in xs:
        soln += x * counter[x]
    return soln
