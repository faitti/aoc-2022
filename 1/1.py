input = [int(x) if x else 0 for x in open("input").read().split("\n")]

def part1():
    e = []
    s = 0
    for l in input:
        if l == 0:
            e.append(s)
            s = 0
        else:
            s += l
    print(f"Part 1: {max(e)}")

def part2():
    e = []
    s = 0
    for l in input:
        if l == 0:
            e.append(s)
            s = 0
        else:
            s += l
    e.sort(reverse = True)
    print(f"Part 2: {sum([e[x] for x in range(0, 3)])}")

part1()
part2()
