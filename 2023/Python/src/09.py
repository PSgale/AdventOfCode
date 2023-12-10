from helpers import readFileLines
import numpy as np


def getNextValue(values, isDebug=False):
    diff = 0
    while True:
        if isDebug:
            print(values)

        values = values[1:] - values[:-1]
        diff += values[-1]

        if np.array_equal(values, np.zeros(len(values))):
            break

    return diff


def getNextValuesHash(file, isDebug=False):
    lines = readFileLines(file)

    total = 0
    for line in lines:
        values = np.array([int(x) for x in line.split(' ')])
        diff = getNextValue(values, isDebug)
        total += values[-1] + diff

        if isDebug:
            print('diff: ', values[-1], ' + ', diff)

    return total


print("%%% Test %%%")
value = getNextValuesHash("09-environmental-instabilities-t1.txt", True)

Expected = 114
print("Sum of extrapolated values: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = getNextValuesHash("09-environmental-instabilities-p1.txt", True)
print("Sum of extrapolated values: ", value)
