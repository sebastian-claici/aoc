from collections import defaultdict, deque
from itertools import combinations

from aocd.models import Puzzle


data = open('day24.in').read()

inputs, ops = data.split("\n\n")

values = {}
for inp in inputs.splitlines():
    label, val = inp.split(":")
    values[label.strip()] = int(val)

operations = []
for line in ops.splitlines():
    inp, out = line.split('->')
    inp, out = inp.strip(), out.strip()
    lhs, op, rhs = inp.split()
    lhs, op, rhs = lhs.strip(), op.strip(), rhs.strip()

    operations.append([lhs, op, rhs, out])

def simulate(ops, values):
    result = []
    queue = deque(ops)
    while queue:
        lhs, op, rhs, out = queue.popleft() 
        if not (lhs in values and rhs in values):
            queue.append([lhs, op, rhs, out])
            continue
    
        match op:
            case 'AND': values[out] = values[lhs] & values[rhs]
            case 'OR': values[out] = values[lhs] | values[rhs]
            case 'XOR': values[out] = values[lhs] ^ values[rhs]
    
        if out[0] == 'z':
            result.append(out)

    result.sort(reverse=True)
    number = []
    for label in result:
        number.append(values[label])
    number = "".join(str(c) for c in number)
    return int(number, 2)

xs = []
ys = []
for key, d in values.items():
    if key[0] == 'x':
        xs.append(key)
    elif key[0] == 'y':
        ys.append(key)

xs.sort(reverse=True)
ys.sort(reverse=True)
x = int("".join(str(values[k]) for k in xs), 2)
y = int("".join(str(values[k]) for k in ys), 2)

z = simulate(operations, values)

s_xy = f"{x+y:046b}"
s_z = f"{z:046b}"

swaps = ['hmt', 'z18', 'bfq', 'z27', 'bng', 'fjp', 'hkh', 'z31']
print(",".join(sorted(swaps)))
