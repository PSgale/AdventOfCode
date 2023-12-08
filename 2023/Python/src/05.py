from helpers import readFileLines
from functools import reduce


def readData(lines, isDebug=False):
    seeds_data = {}

    data = []
    data_new = []
    chapter = ""
    for line in lines:
        # first line should contain seed definitions
        if not seeds_data:
            chapter = "seeds:"
            if line[0:6] == chapter:
                data = [int(x) for x in line[7:].strip().split(" ")]
                seeds_data[chapter] = data
                data_new = [e for e in data]
        else:
            # if line is empty, it should contain chapter or map
            if len(line) > 1:
                # if chapter was retrieved, following lines contain mapping data
                if chapter:
                    data_map = [int(x) for x in line.strip().split(" ")]
                    if isDebug:
                        print(chapter, "[", data_map, "]")
                    for idx, val in enumerate(data):
                        if data_map[1] <= val < data_map[1] + data_map[2]:
                            if isDebug:
                                print(val, idx, 'fit: ', data_map, ' => ', val + data_map[0] - data_map[1])
                            data_new[idx] = val + data_map[0] - data_map[1]

                # if chapter is empty, then line contains a chapter name
                else:
                    chapter = line
            else:
                # if line is empty, chapter get processed
                # store mapped chapter to dictionary
                if chapter:
                    seeds_data[chapter] = data_new
                    if isDebug:
                        print({chapter: data_new})
                    data = data_new
                    data_new = [e for e in data]
                chapter = ""

    # store last mapped chapter
    if chapter:
        seeds_data[chapter] = data_new
        if isDebug:
            print({chapter: data_new})

    return seeds_data


def getLowestLocation(file, isDebug=False):
    lines = readFileLines(file)

    # Map seeds data
    seeds_data = readData(lines, isDebug)

    if isDebug:
        print(seeds_data)

    return reduce(min, seeds_data["humidity-to-location map:"])


print("%%% Test %%%")
value = getLowestLocation("05-seeds-requirements-list-t1.txt", True)

Expected = 35
print("The lowest location number is: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = getLowestLocation("05-seeds-requirements-list-p1.txt")

Expected = 226172555
print("The lowest location number is: ", value)
assert value == Expected, "Not expected result."
