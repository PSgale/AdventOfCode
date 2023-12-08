from numpy.compat import long
from helpers import readFileLines
import numpy as np


def getWinningOptions(file, isDebug=False):
    lines = readFileLines(file)

    time = int(''.join((lines[0].split(":")[1]).split()))
    distance = int(''.join((lines[1].split(":")[1]).split()))

    if isDebug:
        print(time, distance)

    # print(list(range(1, long(distance / time * 10))))

    num_lost = 0
    for sec in range(1, int(distance / time * 10)):
        if sec * (time - sec) <= distance:
            num_lost += 1
        else:
            break

    if isDebug:
        print(num_lost)

    return time - num_lost * 2 - 1


print("%%% Test %%%")
value = getWinningOptions("06-boat-races-list-t1.txt", True)

Expected = 71503
print("Number of ways we can beat the record: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = getWinningOptions("06-boat-races-list-p1.txt")

Expected = 20048741
print("Number of ways we can beat the record: ", value)
assert value == Expected, "Not expected result."
