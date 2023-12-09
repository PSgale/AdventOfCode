from helpers import readFileLines
import re

CUBES = re.compile(r"(\w+)")


def getWinningOptionsHash(file, node_start, node_finish, isDebug=False):
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
    next_node = node_start
    while next_node:
        if isDebug:
            print(next_node)

        if next_node == node_finish:
            break

        next_node = network[next_node][0 if steps[total_steps % len(steps)] == "L" else 1]
        total_steps += 1

    return total_steps


node_start = 'AAA'
node_finish = 'ZZZ'

print("%%% Test %%%")
value = getWinningOptionsHash("08-network-directions-list-t1.txt", node_start, node_finish, True)

Expected = 2
print("Number of steps required to reach ZZZ: ", value)
assert value == Expected, "Not expected result."


print("%%% Test %%%")
value = getWinningOptionsHash("08-network-directions-list-t2.txt", node_start, node_finish)

Expected = 6
print("Number of steps required to reach ZZZ: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = getWinningOptionsHash("08-network-directions-list-p1.txt", node_start, node_finish)

Expected = 17141
print("Number of steps required to reach ZZZ: ", value)
assert value == Expected, "Not expected result."
