from helpers import readFileLines
import numpy as np


def getNodes(lines, isDebug=False):
    nodes = []

    num = 1
    for i, line in enumerate([x for x in lines]):
        for j, char in enumerate([x for x in line]):
            if char == '#':
                nodes.append([i, j, num])
                num += 1
    return nodes


def expandByX(nodes, expansion_factor, isDebug=False):
    nodes.sort(key=lambda x: x[0])
    i = np.array([el[0] for el in nodes])
    i_diff = i[1:] - i[:-1]

    if isDebug:
        print('i_diff: ', i_diff)

    diff = i_diff[0] - 1 if i_diff[0] > 1 else 0
    for idx in range(1, len(nodes)):
        nodes[idx][0] = nodes[idx][0] + diff * (expansion_factor - 1)

        if idx < len(nodes) - 1:
            diff = diff + (i_diff[idx] - 1 if i_diff[idx] > 1 else 0)

    return


def expandByY(nodes, expansion_factor, isDebug=False):
    nodes.sort(key=lambda x: x[1])
    i = np.array([el[1] for el in nodes])
    i_diff = i[1:] - i[:-1]

    if isDebug:
        print('i_diff: ', i_diff)

    diff = i_diff[0] - 1 if i_diff[0] > 1 else 0
    for idx in range(1, len(nodes)):
        nodes[idx][1] = nodes[idx][1] + diff * (expansion_factor - 1)

        if idx < len(nodes) - 1:
            diff = diff + (i_diff[idx] - 1 if i_diff[idx] > 1 else 0)

    return


def getShortestPathsSum(file, expansion_factor, isDebug=False):
    lines = readFileLines(file)

    nodes = getNodes(lines, isDebug)
    if isDebug:
        print('Nodes: ', nodes)

    expandByX(nodes, expansion_factor, isDebug)
    if isDebug:
        print('Nodes: ', nodes)

    expandByY(nodes, expansion_factor, isDebug)
    if isDebug:
        print('Nodes: ', nodes)

    # Calculate distances
    distances_sum = float(0)
    for idx1 in range(len(nodes)):
        for idx2 in range(idx1 + 1, len(nodes)):
            distance = abs(nodes[idx1][0] - nodes[idx2][0]) + abs(nodes[idx1][1] - nodes[idx2][1])
            # print(nodes[idx1][2], nodes[idx2][2], distance)
            distances_sum += distance

    return distances_sum


print("%%% Test %%%")
expansion_factor = 2
value = getShortestPathsSum("11-space-network-t1.txt", expansion_factor, True)

Expected = 374
print("The sum of the shortest paths ( expansion = ", expansion_factor, ") lengths: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
expansion_factor = 1000000
value = getShortestPathsSum("11-space-network-p1.txt", expansion_factor)
print("The sum of the shortest paths ( expansion = ", expansion_factor, ") lengths: ", value)
