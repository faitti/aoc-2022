import sys
input = [tuple(n.split(" ")) for n in open(sys.argv[1]).read().strip().split("\n")]

def part1():
    h = [0, 0]
    t = [0, 0]
    v = dict()
    for (d, n) in input:
        for _ in range(int(n)):
            if d == "R":
                h[0] += 1
                if abs(h[0]-t[0]) > 1:
                    t[0] = h[0] - 1
                    if t[1] != h[1]: t[1] = h[1]
            elif d == "U":
                h[1] += 1
                if abs(h[1]-t[1]) > 1:
                    t[1] = h[1] - 1
                    if t[0] != h[0]: t[0] = h[0]
            elif d == "L":
                h[0] -= 1
                if abs(h[0]-t[0]) > 1:
                    t[0] = h[0] + 1
                    if t[1] != h[1]: t[1] = h[1]
            elif d == "D":
                h[1] -= 1
                if abs(h[1]-t[1]) > 1:
                    t[1] = h[1] + 1
                    if t[0] != h[0]: t[0] = h[0]
            v[tuple(t)] = 1
    print(f"Part 1: {len(v)}")

def part2():
    s = [[0, 0] for _ in range(10)]
    tailpos = set([tuple(s[-1])])
    for (d, n) in input:
        for _ in range(int(n)):
            if d == "L": s[0][0] -= 1
            elif d == "U": s[0][1] += 1
            elif d == "R": s[0][0] += 1
            elif d == "D": s[0][1] -= 1
            for si in range(1, len(s)):
                p = s[si-1]
                c = s[si]
                if max(abs(p[0] - c[0]), abs(p[1] - c[1])) > 1:
                    if p[0] != c[0]: c[0] += (p[0] > c[0] and 1 or -1)
                    if p[1] != c[1]: c[1] += (p[1] > c[1] and 1 or -1)
            tailpos.add(tuple(s[-1]))
    print(f"Part 2: {len(tailpos)}")

part1()
part2()
