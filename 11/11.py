import sys
from collections import defaultdict
from math import prod
input = [x.split("\n") for x in open(sys.argv[1]).read().split("\n\n")]

def parse():
    mks = []
    for m in input:
        mk = []
        for n in range(1, len(m) - 2):
            s = m[n].split(": ")
            if n == 1:
                el = []
                for e in s[-1].split(", "):
                    el.append(int(e))
                mk.append(el)
            elif n == 2:
                mk.append(s[1])
            elif n == 3:
                op = [int(s[-1].split(" ")[-1])]
                op.append(int(m[n + 1].split(" ")[-1]))
                op.append(int(m[n + 2].split(" ")[-1]))
                mk.append(op)
        mks.append(mk)
    return mks

def parts(rr):
    mks = parse()
    ins = defaultdict(int)
    d = 1
    for mk in mks:
        d *= mk[2][0]

    for g in range(rr):
        for x in range(len(mks)):
            mk = mks[x]
            lh = mk[1].split(" = ")[-1].split(" ")
            while len(mk[0]) > 0:
                ins[x] += 1
                n = 0
                if lh[1] == "+":
                    if lh[2] == "old":
                        mk[0][n] += mk[0][n]
                    else:
                        mk[0][n] += int(lh[2])
                elif lh[1] == "*":
                    if lh[2] == "old":
                        mk[0][n] *= mk[0][n]
                    else:
                        mk[0][n] *= int(lh[2])
                if rr == 20:
                    mk[0][n] //= 3 
                else:
                    mk[0][n] %= d
                t = (mk[0][n] % mk[2][0]) == 0
                mks[mk[2][t and 1 or 2]][0].append(mk[0][n])
                mk[0].pop(n)
    print(f"Part {rr == 20 and 1 or 2}:", prod(sorted(list(ins.values()))[-2:]))

parts(20)
parts(10000)

