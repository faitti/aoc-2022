input = [x.split(" ") for x in open("input").read().strip().split("\n")]

op = {'X': 1, 'Y': 2, 'Z': 3}
oop = {'A': 1, 'B': 2, 'C': 3}

def part1():
    s = 0
    for l in input:
        o = l[0]
        m = l[1]
        s += op[m]
        if op[m] == oop[o]:
            s += 3
        elif op[m] - oop[o] in [1, -2]:
            s += 6
    print(f"Part 1: {s}")

def part2():
    s = 0
    lop = {'X': 0, 'Y': 3, 'Z': 6}
    for l in input:
        o = l[0]
        m = l[1]
        s += lop[m]
        for p in ['X', 'Y', 'Z']:
            if lop[m] == 0 and op[p] - oop[o] in [-1, 2]:
                s += op[p]
            elif lop[m] == 3 and op[p] - oop[o] == 0:
                s += op[p]
            elif lop[m] == 6 and op[p] - oop[o] in [1, -2]:
                s += op[p]
    print(f"Part 2: {s}")

part1()
part2()
