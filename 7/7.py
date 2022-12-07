import sys
from collections import defaultdict
input = [x for x in open(sys.argv[1]).read().strip().split("\n")]

def both_parts():
    size = defaultdict(int)
    cwd = []
    for l in input:
        cmd = l.split()
        if cmd[1] == "ls": continue
        if cmd[1] == "cd":
            if cmd[2] == "..": cwd.pop()
            else: cwd.append(cmd[2])
        else:
            try:
                n = int(cmd[0])
                for m in range(len(cwd) + 1):
                    size[''.join(cwd[:m])] += n
            except: pass
    t = 0
    b = sys.maxsize
    nd = size["/"] - 40000000
    for _, v in size.items():
        if v >= nd:
            b = min(b, v)
        if v <= 100000:
            t += v

    print(f"Part 1: {t}")
    print(f"Part 2: {b}")

both_parts()
