import re
input = [x for x in open("input").read().split("\n")]

def parse():
    stacks = [[] for _ in range(9)]
    ins = []
    p = False
    for l in input:
        if "[" in l:
            for n in range(0, len(l), 4):
                c_stack = n == 0 and 0 or (n//4)
                elems = re.findall("\[(.*?)\]", l[n:(n+4)])
                if len(elems) == 0: continue
                stacks[c_stack].append(elems[0])
        else:
            cl = l.split(" ")
            if cl[0] == "move":
                ins.append([int(cl[1]), int(cl[3]) - 1, int(cl[5]) - 1])
    return (stacks, ins)

def part1():
    stacks, ins = parse()
    for l in ins:
        for _ in range(l[0]):
            stacks[l[2]].insert(0, stacks[l[1]].pop(0))
    print(f"Part 1: {''.join([stacks[n][0] for n in range(9) if len(stacks[n]) > 0])}")

def part2():
    stacks, ins = parse()
    for l in ins:
        temp = []
        for _ in range(l[0]):
            temp.insert(0, stacks[l[1]].pop(0))
        for n in range(len(temp)):
            stacks[l[2]].insert(0, temp[n])
    print(f"Part 2: {''.join([stacks[n][0] for n in range(9) if len(stacks[n]) > 0])}")

part1()
part2()
