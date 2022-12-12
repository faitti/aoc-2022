import sys
from collections import deque

def dist(g, s, e):
    vis = {}
    vis[s] = 0
    Q = deque()
    Q.append(s)
    while Q:
        (x, y) = Q.popleft()
        cs = vis[(x, y)]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            (nx, ny) = (x + dx, y + dy)
            if (nx, ny) in vis or nx in [-1, len(g[0])] or ny in [-1, len(g)]: continue
            if ord(g[ny][nx]) - ord(g[y][x]) <= 1:
                vis[(nx, ny)] = cs + 1
                Q.append((nx, ny))
                if (nx, ny) == e:
                    return cs + 1

def parse():
    grid = []
    s = e = (0, 0)
    input = open(sys.argv[1]).read().strip().split("\n")
    for n in range(len(input)):
        grid.append([])
        for m in range(len(input[n])):
            c = input[n][m]
            if c == "S":
                s = (m, n)
                c = 'a'
            elif c == "E":
                e = (m, n)
                c = 'z'
            grid[n].append(c)
    return grid, s, e

def part1():
    grid, s, e = parse()
    print(f"Part 1: {dist(grid, s, e)}")

def part2():
    grid, _, e = parse()
    l = 1e10
    for y in range(len(grid)): 
        for x in range(len(grid[y])):
            if grid[y][x] == 'a':
                cd = dist(grid, (x, y), e)
                if cd and l > cd:
                    l = cd
    print(f"Part 2: {l}")

part1()
part2()
