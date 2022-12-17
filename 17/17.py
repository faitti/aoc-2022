import sys
input = [n for n in open(sys.argv[1]).read().strip()]

def part1():
    towers = set()
    ri, ji = 0, 0
    rocks = (((0, 0), (1, 0), (2, 0), (3, 0)), ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)), ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)), ((0, 0), (0, 1), (0, 2), (0, 3)), ((0, 0), (1, 0), (0, 1), (1, 1)))
    is_empty = lambda x, y: x in range(7) and y > 0 and (x, y) not in towers
    for n in range(2022):
        height = len(towers) > 0 and max(y for (x, y) in towers) or 0
        start = [2, height + 4]
        rock = rocks[ri]
        ri = (ri + 1) % len(rocks)
        while True:
            jet = input[ji] == ">" and 1 or -1
            ji = (ji + 1) % len(input)
            if all(is_empty(start[0] + jet + r[0], start[1] + r[1]) for r in rock): start[0] += jet
            if all(is_empty(start[0] + r[0], start[1] - 1 + r[1]) for r in rock): start[1] -= 1
            else: break
        for r in rock:
            towers.add((start[0] + r[0], start[1] + r[1]))
    print(f"Part 1: {max(y for (x, y) in towers)}")

part1()