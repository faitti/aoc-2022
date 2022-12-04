input = [x.split(",") for x in open("input").read().strip().split("\n")]

def part1():
    s = 0
    for l in input:
        a = l[0].split("-")
        b = l[1].split("-")
        if (int(a[0]) >= int(b[0])) and (int(a[1]) <= int(b[1])):
            s += 1
        elif (int(b[0]) >= int(a[0])) and (int(b[1]) <= int(a[1])):
            s += 1
    print(f"Part 1: {s}")

def part2():
    s = 0
    for l in input:
        a = l[0].split("-")
        b = l[1].split("-")
        if (int(a[0]) >= int(b[0])) and (int(a[1]) <= int(b[1])):
            s += 1
        elif (int(b[0]) >= int(a[0])) and (int(b[1]) <= int(a[1])):
            s += 1
        elif (int(a[0]) >= int(b[0])) and (int(a[0]) <= int(b[1])):
            s += 1
        elif (int(a[1]) >= int(b[0])) and (int(a[1]) <= int(b[1])):
            s += 1
    print(f"Part 2: {s}")

part1()
part2()
