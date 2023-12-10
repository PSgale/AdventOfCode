from helpers import readFileLines
import numpy as np


def getNextValue(values, isDebug=False):
    diff = 0
    i = 0
    while True:
        if isDebug:
            print(values)

        values = values[1:] - values[:-1]
        diff -= values[0] * (1 if i % 2 == 0 else -1)

        if np.array_equal(values, np.zeros(len(values))):
            break
        i += 1

    return diff


def getNextValuesHash(file, isDebug=False):
    lines = readFileLines(file)

    total = 0
    for line in lines:
        values = np.array([int(x) for x in line.split(' ')])
        diff = getNextValue(values, isDebug)
        total += values[0] + diff

        if isDebug:
            print('diff: ', values[0], ' + ', diff)

    return total


print("%%% Test %%%")
value = getNextValuesHash("09-environmental-instabilities-t1.txt", True)

Expected = 2
print("Sum of extrapolated values: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = getNextValuesHash("09-environmental-instabilities-p1.txt", True)
print("Sum of extrapolated values: ", value)
