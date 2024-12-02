from helpers import readFileLines
from collections import Counter

def getDistanceAndSimilarity(file, isDebug = False):
    lines = readFileLines(file)

    a_list = []
    b_list = []
    # Load data
    for str in lines:
        numbers = str.split('  ')
        a_list.append(int(numbers[0]))
        b_list.append(int(numbers[1]))

    # Sort elements in lists for distance calculation
    a_list.sort()
    b_list.sort()

    # Calculate frequency of elements in list b_list
    b_list_to_frequencies = Counter(b_list)

    total_distance = 0
    total_similarity = 0
    # Calculate distance and similarity
    for a, b in zip(a_list, b_list):
        total_distance += abs(a - b)
        total_similarity += a * b_list_to_frequencies[a]

    if (isDebug):
        print(a_list)
        print(b_list)

    return [total_distance, total_similarity]


print("%%% Test %%%")
value1, value2 = getDistanceAndSimilarity("01-two-list-locations-t1.txt", True)

Expected = 11
print("Distance: ", value1)
print("Similarity: ", value2)
assert value1 == Expected, "Not expected result."


print("%%% Unit %%%")
value1, value2 = getDistanceAndSimilarity("01-two-list-locations-p1.txt")
print("Distance: ", value1)
print("Similarity: ", value2)