import re

from aocd.models import Puzzle


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]


puzzle = Puzzle(year=2024, day=17)
data = puzzle.input_data


registers, program = data.split("\n\n")

regs = []
for line in registers.split("\n"):
    regs.append(int(line.split(":")[1]))
a, b, c = regs

ptr = 0
program = ints(program)


def run_program(program, a, b, c):
    ptr = 0
    outputs = []

    while ptr < len(program):
        inst, op = program[ptr], program[ptr + 1]

        val = 0
        if op <= 3:
            val = op
        if op == 4:
            val = a
        if op == 5:
            val = b
        if op == 6:
            val = c

        match inst:
            case 0:
                a = a // (1 << val)
                ptr += 2
            case 1:
                b = b ^ op
                ptr += 2
            case 2:
                b = val % 8
                ptr += 2
            case 3:
                if a != 0:
                    ptr = op
                else:
                    ptr += 2
            case 4:
                b = b ^ c
                ptr += 2
            case 5:
                outputs.append(val % 8)
                ptr += 2
            case 6:
                b = a // (1 << val)
                ptr += 2
            case 7:
                c = a // (1 << val)
                ptr += 2

    return outputs


# run_program(program, a, b, c)

print(len(program))
print(",".join(str(c) for c in program))


def get_val(a, b, c):
    b = (a % 8) ^ 5
    c = a // (1 << b)
    b = b ^ 6
    b = b ^ c
    return b % 8


a = 0

can = set()
can.add(0)
for num in reversed(program):
    new_can = set()
    for curr in can:
        for k in range(8):
            try_val = (curr << 3) + k
            if get_val(try_val, b, c) == num:
                new_can.add(try_val)
    can = new_can

a = min(can)
print(a)
print(",".join(str(c) for c in program))
print(",".join(str(c) for c in run_program(program, a, b, c)))
