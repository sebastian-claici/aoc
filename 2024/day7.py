import itertools
import re

from aocd.models import Puzzle


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


puzzle = Puzzle(year=2024, day=7)
data = puzzle.input_data
lines = [line.strip() for line in data.split("\n")]

soln = 0
for line in lines:
    t, rest = line.split(":")
    t = int(t)
    nums = ints(rest)

    ops = ["+", "*", "||"]
    for op_vals in itertools.product(ops, repeat=len(nums) - 1):
        val = nums[0]
        for i in range(1, len(nums)):
            match op_vals[i - 1]:
                case "+":
                    val += nums[i]
                case "*":
                    val *= nums[i]
                case "||":
                    val = int(f"{val}{nums[i]}")
        if val == t:
            soln += val
            break

print(soln)
