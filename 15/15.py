import sys
import math
from collections import defaultdict
input = [n.split(" ") for n in open(sys.argv[1]).read().strip().split("\n")]

def dist(x, y, x2, y2):
    return abs(x - x2) + abs(y - y2)

def part1():
    b = defaultdict(lambda: " ")
    for l in input:
        sx, sy = int(l[2].split("=")[-1][:-1]), int(l[3].split("=")[-1][:-1])
        bx, by = int(l[-2].split("=")[-1][:-1]), int(l[-1].split("=")[-1])
        b[(sx, sy)] = "S"
        b[(bx, by)] = "B"
        di = dist(sx, sy, bx, by)
        for d in range(0, di):
            if dist(sx, sy, sx + d, 2000000) <= di:
                if b[(sx + d, 2000000)] == " ":
                    b[(sx + d, 2000000)] = "#"
                if b[(sx -d, 2000000)] == " ":
                    b[(sx - d, 2000000)] = "#"
    a = 0
    for k in b:
        if b[k] == "#":
            a += 1
    print(f"Part 1: {a}")

def part2():
    w = 4000000
    scs = {}
    for l in input:
        sx, sy = int(l[2].split("=")[-1][:-1]), int(l[3].split("=")[-1][:-1])
        bx, by = int(l[-2].split("=")[-1][:-1]), int(l[-1].split("=")[-1])
        di = dist(sx, sy, bx, by)
        scs[(sx, sy, di)] = 1
    for sx, sy, di in scs:
        for n in range(di + 1):
            for dx, dy in [(sx - di - 1 + n, sy - n), (sx + di + 1 - n, sy -n), (sx - di - 1 + n, sy + n), (sx + di + 1 - n, sy + n)]:
                if 0 <= dx <= w and 0 <= dy <= w and all(dist(dx, dy, fx, fy) > fd for fx, fy, fd in scs):
                    print(f"Part 2: {dx * w + dy}")
                    sys.exit(0)

part1()
part2()
