from functools import lru_cache
from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=11)
data = puzzle.input_data
stones = [int(c) for c in data.split()]


@lru_cache(maxsize=None)
def simulate(stone, rounds):
    if rounds == 0:
        return 1
    if stone == 0:
        return simulate(1, rounds - 1)

    ans = 0
    s = str(stone)
    if len(s) % 2 == 0:
        ans += simulate(int(s[: len(s) // 2]), rounds - 1)
        ans += simulate(int(s[len(s) // 2 :]), rounds - 1)
        return ans
    else:
        return simulate(2024 * stone, rounds - 1)


p1, p2 = 0, 0
for stone in stones:
    p1 += simulate(stone, 25)
    p2 += simulate(stone, 75)

print(p1)
print(p2)
