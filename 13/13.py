import sys
from functools import cmp_to_key
input = [list(map(eval, n.split("\n"))) for n in open(sys.argv[1]).read().strip().split("\n\n")]

def compare(l, r):
    tl, tr = type(l), type(r)
    if tl == int and tr == int:
        if l < r: return -1
        elif l > r: return 1
        else: return 0
    if tl == int and tr == list: return compare([l], r)
    if tl == list and tr == int: return compare(l, [r])
    if tl == list and tr == list:
        if (len(l) == len(r)):
            for n, m in zip(l, r):
                v = compare(n, m)
                if v != 0: return v
            return 0
        else:
            ix = 0
            while ix < len(l) and ix < len(r):
                n, m = l[ix], r[ix]
                v = compare(n, m)
                if v != 0: return v
                ix += 1
            if len(l) < len(r): return -1
            else: return 1
    return 0

def part1():
    s = 0
    for m in range(len(input)):
        if compare(*input[m]) == -1: s += m + 1
    print(f"Part 1: {s}")

def part2():
    ninput = [[[2]], [[6]]]
    for n, m in input:
        ninput.append(n)
        ninput.append(m)
    xx = len(ninput)
    for e in range(xx - 1):
        for r in range(0, xx - e - 1):
            if compare(ninput[r], ninput[r + 1]) == 1:
                ninput[r], ninput[r + 1] = ninput[r + 1], ninput[r]
    print(f"Part 2: {(ninput.index([[2]]) + 1) * (ninput.index([[6]]) + 1)}")

part1()
part2()
