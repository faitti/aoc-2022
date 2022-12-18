import sys
input = set([tuple(list(map(int, n.split(",")))) for n in open(sys.argv[1]).read().strip().split("\n")])

def part1():
    ans = 0
    for (x, y, z) in input:
        if (x + 1, y, z) not in input:
            ans += 1
        if (x, y + 1, z) not in input:
            ans += 1
        if (x, y, z + 1) not in input:
            ans += 1
        if (x - 1, y, z) not in input:
            ans += 1
        if (x, y - 1, z) not in input:
            ans += 1
        if (x, y, z - 1) not in input:
            ans += 1
    print(f"Part 1: {ans}")

part1()
