import re
from sympy import symbols, Eq, solve

from aocd.models import Puzzle

def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]

puzzle = Puzzle(year=2024, day=13)
data = puzzle.input_data
rounds = data.split("\n\n")

part2 = True
soln = 0
for round in rounds:
    lines = round.split("\n")
    x1, y1 = ints(lines[0])
    x2, y2 = ints(lines[1])
    r1, r2 = ints(lines[2])
    if part2:
        r1 += 10000000000000
        r2 += 10000000000000

    a, b = symbols('a b', integer=True)
    vars = [a, b]
    constraints = [
        Eq(a * x1 + b * x2, r1),
        Eq(a * y1 + b * y2, r2)
    ]
    solutions = solve(constraints, *vars, dict=True)
    if solutions:
        soln += min(3 * sol[a] + sol[b] for sol in solutions)

print(soln)
