import sys
input = [l.split(" ") for l in open(sys.argv[1]).read().strip().split("\n")]

def find_depth(tunnels, key, valves):
    depth = 0
    while True:
        depth += 1
        next_tunnels = set()
        for tunnel in tunnels:
            if tunnel == key:
                return depth
            for _tunnel in valves[tunnel][1]:
                next_tunnels.add(_tunnel)
        tunnels = next_tunnels

def parse():
    valves = dict()
    for l in input:
        valves[l[1]] = [int(l[4].split("=")[-1][:-1]), ''.join(l[9:]).split(","), {}]
    keys = list(valves.keys())
    return valves, keys

ans = 0
def search(open_valves, flow, tunnel, d, valves):
    global ans
    ans = max(ans, flow)
    if d <= 0: return
    if tunnel not in open_valves:
        search(open_valves | set([tunnel]), flow + valves[tunnel][0] * d, tunnel, d - 1, valves)
    else:
        for key in [k for k in valves[tunnel][2].keys() if k not in open_valves]:
            search(open_valves, flow, key, d - valves[tunnel][2][key], valves)


def part1():
    global ans
    valves, keys = parse()
    ans = 0
    for key in keys:
        for _key in keys:
            if valves[_key][0] == 0: continue
            if key == _key: continue
            valves[key][2][_key] = find_depth(valves[key][1], _key, valves)
    first_key = sorted([k for k in valves.keys()])[0]
    search(set([first_key]), valves[first_key][0], first_key, 29, valves)
    print(f"Part 1: {ans}")

part1()