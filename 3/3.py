input1 = [[x[:len(x)//2], x[len(x)//2:]] for x in open("input").read().strip().split("\n")]
input2 = [x for x in open("input").read().strip().split("\n")]

def part1():
    s = 0
    for l in input1:
        for c in l[0]:
            if c in l[1]:
                s += ord(c.lower()) - 96
                if c != c.lower(): s += 26
                break

    print(f"Part 1: {s}")

def part2():
    s = 0
    for n in range(3, len(input2) + 3, 3):
        c = input2[(0 + (n - 3)): n]
        for cr in c[0]:
            if (cr in c[1]) and (cr in c[2]):
                s += ord(cr.lower()) - 96
                if cr != cr.lower(): s += 26
                break

    print(f"Part 2: {s}")

part1()
part2()
