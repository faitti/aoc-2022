import sys
input = [[c for c in r] for r in open(sys.argv[1]).read().strip().split("\n")]

def part1():
    s = 2 * len(input[0]) + 2 * (len(input[0]) - 2)
    for r in range(1, len(input) - 1):
        for c in range(1, len(input[r]) - 1):
            e = input[r][c]
            l = input[r][:c]
            rr = input[r][c+1:]
            t = [v[c] for v in input]
            tt = t[:r]
            tb = t[r+1:]
            if e > max(l) or e > max(rr) or e > max(tt) or e > max(tb): s += 1
    print(f"Part 1: {s}")
           
def part2():
    b = 0
    for n in range(len(input)):
        for m in range(len(input[n])):
            l = r = t = bt = 0
            e = input[n][m]
            for x in range(m -1, -1, -1):
                l += 1
                if input[n][x] >= e: break
            for x in range(m + 1, len(input[n])):
                r += 1
                if input[n][x] >= e: break
            for x in range(n - 1, -1, -1):
                t += 1
                if input[x][m] >= e: break
            for x in range(n + 1, len(input[n])):
                bt += 1
                if input[x][m] >= e: break
            b = max(b, l * r * t * bt)
    print(f"Part 2: {b}")

part1()
part2()
