from helpers import readFileLines
from collections import Counter
import re

def getDistance(file, isDebug = False):
    lines = readFileLines(file)

    a = []
    b = []
    # Load data
    for str in lines:
        numbers = str.split('  ')
        a.append(int(numbers[0]))
        b.append(int(numbers[1]))

    # Sort elements in lists for distance calculation
    a.sort()
    b.sort()

    # Calculate frequency of elements in list b
    key_b = Counter(b)

    total_distance = 0
    total_similarity = 0
    # Calculate distance
    for i, val_a in enumerate(a):
        val_b = b[i]

        total_distance += abs(val_a - val_b)
        total_similarity += val_a * key_b[val_a]

    if (isDebug):
        print(a)
        print(b)

    return [total_distance, total_similarity]


print("%%% Test %%%")
value1, value2 = getDistance("01-two-list-locations-t1.txt", True)

Expected = 11
print("Distance: ", value1)
print("Similarity: ", value2)
assert value1 == Expected, "Not expected result."


print("%%% Unit %%%")
value1, value2 = getDistance("01-two-list-locations-p1.txt")
print("Distance: ", value1)
print("Similarity: ", value2)