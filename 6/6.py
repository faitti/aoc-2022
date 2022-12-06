import sys
input = open(len(sys.argv) > 1 and sys.argv[1] or "input").read().strip()

def part1():
    for l in range(len(input) - 3):
        ch = input[l:(l+4)]
        if len(set(ch)) == 4:
            print(f"Part 1: {l + 4}")
            break

def part2():
    for l in range(len(input) - 13):
        ch = input[l:(l+14)]
        if len(set(ch)) == 14:
            print(f"Part 2: {l + 14}")
            break

part1()
part2()
