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


def getStartPipe(direction_from_start, direction_to_start):
    if direction_to_start == "W" and direction_from_start == "S" or direction_to_start == "N" and direction_from_start == "E":
        return "F"
    elif direction_to_start == "W" and direction_from_start == "N" or direction_to_start == "S" and direction_from_start == "E":
        return "L"
    elif direction_to_start == "W" and direction_from_start == "W" or direction_to_start == "E" and direction_from_start == "E":
        return "-"
    elif direction_to_start == "E" and direction_from_start == "S" or direction_to_start == "N" and direction_from_start == "W":
        return "7"
    elif direction_to_start == "E" and direction_from_start == "N" or direction_to_start == "S" and direction_from_start == "W":
        return "J"
    elif direction_to_start == "N" and direction_from_start == "N" or direction_to_start == "S" and direction_from_start == "S":
        return "|"


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



def isEnclosed(borders_left, isDebug=False):
    border_num = 0
    border_prev = ""
    for border in borders_left:
        if border_prev == "F" and border[1] == "J" or border_prev == "L" and border[1] == "7":
            border_prev = ""
        else:
            border_num += 1
            border_prev = border[1]

    return border_num % 2 == 1


def isEnclosed_2(borders_left, isDebug=False):
    border_num = 0
    border_prev = ""
    for border in borders_left:
        if border[1] == "|":
            border_num += 1

        if border_prev == "F" and border[1] == "J" or border_prev == "L" and border[1] == "7":
            border_num += 1

        border_prev = border[1]

    return border_num % 2 == 1


def getEnclosedTiles(file, isDebug=False):
    lines = readFileLines(file)
    path = {}
    borders = [[] for _ in range(len(lines))]

    # Identify Start point
    next_point = getStartNode(lines)
    path[str(next_point[0][0]) + "_" + str(next_point[0][1])] = next_point[1]
    if next_point[1] != "-":
        borders[next_point[0][0]].append([next_point[0][1], next_point[1]])

    # Get direction from Start
    direction, next_point = getDirection(next_point, lines, "*")
    path[str(next_point[0][0]) + "_" + str(next_point[0][1])] = next_point[1]
    if next_point[1] != "-":
        borders[next_point[0][0]].append([next_point[0][1], next_point[1]])
    direction_from_start = direction

    # Identify path
    iteration = 0
    while True:
        direction_to_start = direction
        direction, next_point = getDirection(next_point, lines, direction)
        if next_point[1] == "S":
            break

        path[str(next_point[0][0]) + "_" + str(next_point[0][1])] = next_point[1]
        if next_point[1] != "-":
            borders[next_point[0][0]].append([next_point[0][1], next_point[1]])
        iteration += 1

    # Update start pipe
    # if isDebug:
    #     print("S:", direction_from_start, direction_to_start, getStartPipe(direction_from_start, direction_to_start))

    for key in path:
        if path[key] == 'S':
            path[key] = getStartPipe(direction_from_start, direction_to_start)
            i = int(key[0])
            for j, line_i in enumerate(borders[int(key[0])]):
                if borders[i][j][1] == "S":
                    borders[i][j][1] = getStartPipe(direction_from_start, direction_to_start)

    # Calculate Enclosed Tiles
    total = 0
    for i in range(len(lines)):
        # rows with path
        if borders[i]:
            for j in range(len(lines[0])):
                # nodes does not belong to path
                if not "_".join([str(i), str(j)]) in path:
                    # has borders from the left
                    borders_left = sorted([s for s in borders[i] if s[0] < j])
                    borders_right = sorted([s for s in borders[i] if s[0] > j])
                    if borders_left and borders_right:

                        if isDebug:
                            print("_".join([str(i), str(j)]), lines[i][j], borders_left, isEnclosed(borders_left, isDebug), isEnclosed_2(borders_left, isDebug))

                        if isEnclosed_2(borders_left, isDebug):
                            total += 1
                            # if isDebug:

    if isDebug:
        print('path: ', path)
        print('borders: ', borders)

    return total


print("%%% Test %%%")
value = getEnclosedTiles("10-pipe-network-t1.txt", True)

Expected = 1
print("Number of tiles enclosed by the loop: ", value)
assert value == Expected, "Not expected result."


print("%%% Test %%%")
value = getEnclosedTiles("10-pipe-network-t2.txt", True)

Expected = 1
print("Number of tiles enclosed by the loop: ", value)
assert value == Expected, "Not expected result."


print("%%% Test %%%")
value = getEnclosedTiles("10-pipe-network-t3.txt", True)

Expected = 8
print("Number of tiles enclosed by the loop: ", value)
assert value == Expected, "Not expected result."


print("%%% Test %%%")
value = getEnclosedTiles("10-pipe-network-t4.txt", True)

Expected = 10
print("Number of tiles enclosed by the loop: ", value)
assert value == Expected, "Not expected result."

print("%%% Unit %%%")
value = getEnclosedTiles("10-pipe-network-p1.txt")
print("Number of tiles enclosed by the loop: ", value)
