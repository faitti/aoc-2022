import sys
input = [n for n in open(sys.argv[1]).read().strip().split("\n")]

def grid():
    blocked = set()
    a = 0
    for l in input:
        inp = [list(map(int, c.split(","))) for c in l.strip().split(" -> ")]
        for (x, y), (xx, yy) in zip(inp, inp[1:]):
            x, xx = sorted([x, xx])
            y, yy = sorted([y, yy])
            for n in range(x, xx + 1):
                for m in range(y, yy + 1):
                    blocked.add((n, m))
                    a = max(a, m + 1)
    return blocked, a

def part1():
    blocked, a = grid()
    ans = 0
    try:
        while True:
            sp = [500, 0]
            while True:
                if sp[1] >= a:
                    raise RuntimeError
                if (sp[0], sp[1] + 1) not in blocked:
                    sp[1] += 1
                    continue
                if (sp[0] - 1, sp[1] + 1) not in blocked:
                    sp[0] -= 1
                    sp[1] += 1
                    continue
                if (sp[0] + 1, sp[1] + 1) not in blocked:
                    sp[0] += 1
                    sp[1] += 1
                    continue
                blocked.add((sp[0], sp[1]))
                ans += 1
                break
    except RuntimeError:
        print(f"Part 1: {ans}")
    
def part2():
    blocked, a = grid()
    ans = 0
    while (500, 0) not in blocked:
        sp = [500, 0]
        while True:
            if sp[1] >= a:
                break
            if (sp[0], sp[1] + 1) not in blocked:
                sp[1] += 1
                continue
            if (sp[0] - 1, sp[1] + 1) not in blocked:
                sp[0] -= 1
                sp[1] += 1
                continue
            if (sp[0] + 1, sp[1] + 1) not in blocked:
                sp[0] += 1
                sp[1] += 1
                continue
            break
        blocked.add((sp[0], sp[1]))
        ans += 1
    print(f"Part 2: {ans}")

part1()
part2()
