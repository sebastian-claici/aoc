from collections import Counter

from aocd import data

lines = data.split("\n")

xs, ys = [], []
for line in lines:
    nums = [int(x) for x in line.split()]
    xs.append(nums[0])
    ys.append(nums[1])
xs.sort()
ys.sort()


def p1(xs, ys):
    return sum(abs(x - y) for x, y in zip(xs, ys))


def p2(xs, ys):
    counter = Counter(ys)
    return sum(x * counter[x] for x in xs)


print(p1(xs, ys))
print(p2(xs, ys))
