from helpers import readFileLines, lcm
from functools import reduce
import re

CUBES = re.compile(r"(\w+)")


def getWinningOptionsHash(file, isDebug=False):
    lines = readFileLines(file)
    network = {}

    steps = [x for x in lines[0]]

    for line in lines[2:]:
        node, nodeL, nodeR = CUBES.findall(line)
        network[node] = [nodeL, nodeR]

    if isDebug:
        print(steps)
        print(network)

    total_steps = 0
    next_nodes = [x for x in network.keys() if x[-1] == 'A']
    stepsToZ = {}
    while True:
        for item in [x for x in next_nodes if x[-1] == 'Z']:
            stepsToZ[item] = total_steps

        if isDebug:
            print(next_nodes)
            print(stepsToZ)

        # Every node has own cycle. When nodes endup in node with Z we will calculate with LCM.
        if len(stepsToZ) == len(next_nodes):
            break

        next_nodes = [network[x][0 if steps[total_steps % len(steps)] == "L" else 1] for x in next_nodes]
        total_steps += 1

    return reduce(lambda a, b: lcm(a, b), stepsToZ.values())


print("%%% Test %%%")
value = getWinningOptionsHash("08-network-directions-list-t3.txt", True)

Expected = 6
print("Number of steps required to nodes that end with Z: ", value)
assert value == Expected, "Not expected result."

print("%%% Unit %%%")
value = getWinningOptionsHash("08-network-directions-list-p1.txt")

Expected = 10818234074807
print("Number of steps required to nodes that end with Z: ", value)
assert value == Expected, "Not expected result."
