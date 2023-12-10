from helpers import readFileLines
import numpy as np


def getWinningOptionsHash(file, isDebug=False):
    lines = readFileLines(file)
    numbers = []

    for line in lines:
        label_, numbers_ = line.split(":")
        numbers.append([int(x) for x in (' '.join(numbers_.split()).split(' '))])

    if isDebug:
        print(numbers)

    total = 1
    for race in zip(numbers[0], numbers[1]):
        winning_options = len([item for item in np.arange(1, race[0], 1, dtype=int) * (race[0] - np.arange(1, race[0], 1, dtype=int)) if item > race[1]])
        total = total * winning_options

        if isDebug:
            print(np.arange(1, race[0], 1, dtype=int) * (race[0] - np.arange(1, race[0], 1, dtype=int)))

    return total


print("%%% Test %%%")
value = getWinningOptionsHash("06-boat-races-list-t1.txt", True)

Expected = 288
print("We get if multiply these numbers together: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = getWinningOptionsHash("06-boat-races-list-p1.txt")
print("We get if multiply these numbers together: ", value)
