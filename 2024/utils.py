import re


def ints(line: str):
    return [int(x) for x in re.findall(r"-?\d+", line)]
