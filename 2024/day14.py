import re
from collections import deque, defaultdict

from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=14)
data = puzzle.input_data

def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]

def simulate(robot, grid_x=101, grid_y=103, secs=100):
    px, py, vx, vy = robot
    px = (px + secs * vx) % grid_x
    py = (py + secs * vy) % grid_y

    mid_x = grid_x // 2
    mid_y = grid_y // 2
    if px == mid_x or py == mid_y:
        return -1

    quad = (int(px < mid_x) << 1) | int(py < mid_y)
    return quad


def display(robots, grid_x=101, grid_y=103):
    grid = [['.' for _ in range(grid_x)] for _ in range(grid_y)]
    for (px, py, _, _) in robots:
        grid[py][px] = 'x'
    for line in grid:
        print("".join(line))


ans = defaultdict(int)
robots = []
for line in data.split("\n"):
    px, py, vx, vy = ints(line)
    robots.append((px, py, vx, vy))
    quad = simulate((px, py, vx, vy), 101, 103) 
    if quad != -1:
        ans[quad] += 1

val = 1
for k, v in ans.items():
    if k == -1:
        continue
    val *= v
print(val)

check = 114
checks = set()
for _ in range(1000):
    checks.add(check)
    check += 101

for s in range(0, 100000, 1):
    if s in checks:
        display(robots)
        print(s)
        input()
    for i, (px, py, vx, vy) in enumerate(robots):
        robots[i] = ((px + vx) % 101, (py + vy) % 103, vx, vy)
