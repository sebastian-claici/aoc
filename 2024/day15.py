from collections import deque, defaultdict

from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=15)
data = puzzle.input_data

replace = {"#": "##", "O": "[]", ".": "..", "@": "@."}
grid, moves = data.split("\n\n")
grid = [[c for c in line.strip()] for line in grid.split("\n")]
moves = [c for c in moves if c in ["<", ">", "v", "^"]]

adj = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}


def show(grid):
    for line in grid:
        print("".join(line))


def bfs_move(grid, sx, sy, d):
    q = deque([(sx, sy)])
    visited = set()
    dx, dy = adj[d]
    while q:
        x, y = q.popleft()
        visited.add((x, y))
        nx, ny = x + dx, y + dy
        if grid[nx][ny] == "#":
            return sx, sy
        if grid[nx][ny] != ".":
            q.append((nx, ny))
        if grid[nx][ny] == "]" and (nx, ny - 1) not in visited:
            q.append((nx, ny - 1))
        if grid[nx][ny] == "[" and (nx, ny + 1) not in visited:
            q.append((nx, ny + 1))

    while visited:
        for x, y in visited:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited:
                grid[nx][ny] = grid[x][y]
                grid[x][y] = "."
                visited.remove((x, y))
                break
    return sx + dx, sy + dy


def part1(grid):
    sx, sy = 0, 0
    for x, line in enumerate(grid):
        for y, c in enumerate(line):
            if c == "@":
                sx, sy = x, y

    visited = set([(sx, sy)])
    for move in moves:
        sx, sy = bfs_move(grid, sx, sy, move)
        visited.add((sx, sy))

    ans = 0
    for x, line in enumerate(grid):
        for y, c in enumerate(line):
            if c == "O":
                ans += 100 * x + y
    print(ans)


def part2(grid):
    for i, line in enumerate(grid):
        line = "".join([replace[c] for c in line])
        grid[i] = [c for c in line]

    sx, sy = 0, 0
    for x, line in enumerate(grid):
        for y, c in enumerate(line):
            if c == "@":
                sx, sy = x, y

    for move in moves:
        sx, sy = bfs_move(grid, sx, sy, move)

    ans = 0
    for x, line in enumerate(grid):
        for y, c in enumerate(line):
            if c == "[":
                ans += 100 * x + y
    print(ans)


part2(grid)
