from helpers import readFileLines
import numpy as np


def getStartNode(lines, isDebug=False):

    for i, line in enumerate([x for x in lines]):
        for j, val in enumerate([x for x in line]):
            if isDebug:
                print([np.array([i, j]), val])
            if val == "S":
                return [np.array([i, j]), val]

    return [np.array([-1, -1]), ""]

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this


def getDirection(position, lines, direction, isDebug=False):
    i = position[0][0]
    j = position[0][1]
    # Check North
    if i - 1 >= 0 and (direction == "N" or direction == "*"):
        value = lines[i - 1][j]
        if isDebug:
            print("North", [np.array([i - 1, j]), value])
        if value == "|" or value == "7" or value == "F" or value == "S":
            if value == "|":
                direction = "N"
            elif value == "7":
                direction = "W"
            elif value == "F":
                direction = "E"
            else:
                direction = "*"
            return direction, [np.array([i - 1, j]), value]
    # Check South
    if i + 1 < len(lines) and (direction == "S" or direction == "*"):
        value = lines[i + 1][j]
        if isDebug:
            print("South", [np.array([i - 1, j]), value])
        if value == "|" or value == "J" or value == "L" or value == "S":
            if value == "|":
                direction = "S"
            elif value == "J":
                direction = "W"
            elif value == "L":
                direction = "E"
            else:
                direction = "*"
            return direction, [np.array([i + 1, j]), value]
    # Check East
    if j + 1 >= 0 and (direction == "E" or direction == "*"):
        value = lines[i][j + 1]
        if isDebug:
            print("East", [np.array([i - 1, j]), value])
        if value == "-" or value == "J" or value == "7" or value == "S":
            if value == "-":
                direction = "E"
            elif value == "J":
                direction = "N"
            elif value == "7":
                direction = "S"
            else:
                direction = "*"
            return direction, [np.array([i, j + 1]), value]
    # Check West
    if j - 1 < len(lines[0]) and (direction == "W" or direction == "*"):
        value = lines[i][j - 1]
        if isDebug:
            print("West", [np.array([i - 1, j]), value])
        if value == "-" or value == "L" or value == "F" or value == "S":
            if value == "-":
                direction = "W"
            elif value == "L":
                direction = "N"
            elif value == "F":
                direction = "S"
            else:
                direction = "*"
            return direction, [np.array([i, j - 1]), value]

    return "*", [np.array([-1, -1]), ""]


def getFarthestPosition(file, isDebug=False):
    lines = readFileLines(file)
    path = []

    next_point = getStartNode(lines)
    if isDebug:
        print('next_point: ', next_point)
    path.append(next_point)

    direction, next_point = getDirection(next_point, lines, "*")
    if isDebug:
        print('next_point: ', next_point)
    path.append(next_point)

    iteration = 0
    while True:
        direction, next_point = getDirection(next_point, lines, direction)
        if isDebug:
            print('next_point: ', next_point)
        if next_point[1] == "S":
            break

        path.append(next_point)
        iteration += 1

    if isDebug:
        print('path: ', path)

    return int(len(path) / 2)


print("%%% Test %%%")
value = getFarthestPosition("10-pipe-network-t1.txt", True)

Expected = 4
print("# steps along the loop to get from the starting position to the point farthest from the starting position: ", value)
assert value == Expected, "Not expected result."


print("%%% Test %%%")
value = getFarthestPosition("10-pipe-network-t2.txt")

Expected = 8
print("# steps along the loop to get from the starting position to the point farthest from the starting position: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = getFarthestPosition("10-pipe-network-p1.txt")
print("# steps along the loop to get from the starting position to the point farthest from the starting position: ", value)
