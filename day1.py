from collections import defaultdict

from aocd import data, submit


def solve():
    return 0


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
    submit(str(soln))


def p2(xs, ys):
    counter = defaultdict(int)
    for y in ys:
        counter[y] += 1

    soln = 0
    for x in xs:
        soln += x * counter[x]
    submit(str(soln))


p2(xs, ys)
