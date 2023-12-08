from helpers import readFileLines
from functools import reduce


def mapData(data, chapter, data_map, isDebug=False):
    data_new = []

    idx = 0
    while idx < len(data):
        for map_ in data_map:
            range_x = data[idx][0]
            range_y = data[idx][1]

            map_x = map_[1]
            map_y = map_[1] + map_[2] - 1
            map_dif = map_[0] - map_[1]

            # if range inside the map
            # if map_x < range_x and map_y > range_y:
            #     if isDebug:
            #         print("- range ", data[idx], " - ", map_, " inside the map ")
            # if range covers left border
            if map_x < range_x <= map_y < range_y:
                if isDebug:
                    print("- range ", data[idx], " - ", map_, " covers left border ")
                data.append([range_x, map_y])
                if map_y < range_y:
                    data.append([map_y + 1, range_y])
                del data[idx]
                continue
            # if range covers right border
            elif range_x < map_x <= range_y < map_y:
                if isDebug:
                    print("- range ", data[idx], " - ", map_, " covers right border ")
                if range_x < map_x:
                    data.append([range_x, map_x - 1])
                data.append([map_x, range_y])
                del data[idx]
                continue
            # if range covers the map
            elif range_x <= map_x <= map_y < range_y or range_x < map_x <= map_y <= range_y or range_x < map_x <= map_y < range_y:
                if isDebug:
                    print("- range ", data[idx], " - ", map_, " covers the map ")
                if range_x < map_x:
                    data.append([range_x, map_x - 1])
                data.append([map_x, map_y])
                if map_y < range_y:
                    data.append([map_y + 1, range_y])
                del data[idx]
                continue
            # else:
            #     if isDebug:
            #         print("- range ", data[idx], " - ", map_, " not mapped ")

        idx += 1

    if isDebug:
        print({chapter: data})

    for range_ in data:
        range_x = range_[0]
        range_y = range_[1]
        is_mapped = False

        for map_ in data_map:
            map_x = map_[1]
            map_y = map_[1] + map_[2] - 1
            map_dif = map_[0] - map_[1]

            # if range inside the map
            if map_x <= range_x and map_y >= range_y:
                if isDebug:
                    print("= range ", range_, " inside the map ", map_, " => ", map_dif)
                is_mapped = True
                data_new.append([range_x + map_dif, range_y + map_dif])

        if not is_mapped:
            if isDebug:
                print("= not mapped, add original range ", range_)
            data_new.append([range_x, range_y])

    return data_new


def readData(lines, isDebug=False):
    seeds_data = {}

    data = []
    data_new = []
    data_map = []
    chapter = ""
    for line in lines:
        # first line should contain seed definitions
        if not seeds_data:
            chapter = "seeds:"
            if line[0:6] == chapter:
                tmp = [int(x) for x in line[7:].strip().split(" ")]
                data = []
                for i in range(0, len(tmp), 2):
                    data.append([tmp[i], tmp[i] + tmp[i+1] - 1])

                seeds_data[chapter] = data

                if isDebug:
                    print({chapter: data})
        else:
            # if line is empty, it should contain chapter or map
            if len(line) > 1:
                # if chapter was retrieved, following lines contain mapping data
                if chapter:
                    data_map.append([int(x) for x in line.strip().split(" ")])

                # if chapter is empty, then line contains a chapter name
                else:
                    chapter = line
            else:
                # if line is empty, chapter get processed
                # store mapped chapter to dictionary
                if chapter and chapter != "seeds:":
                    data_map.sort(key=lambda row: (row[1]))
                    if isDebug:
                        print(chapter, ".", data_map, "")

                    data_new = mapData(data, chapter, data_map, isDebug)

                    seeds_data[chapter] = data_new
                    if isDebug:
                        print({chapter: data_new})
                    data = [e for e in data_new]

                chapter = ""
                data_map = []

    # store last mapped chapter
    if chapter:
        data_map.sort(key=lambda row: (row[1]))
        if isDebug:
            print(chapter, ".", data_map, "")

        data_new = mapData(data, chapter, data_map, isDebug)
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

    return sorted(seeds_data["humidity-to-location map:"])[0]


print("%%% Test %%%")
value = getLowestLocation("05-seeds-requirements-list-t1.txt", True)

Expected = 46
print("The lowest location number is: ", value)
# assert value[0] == Expected, "Not expected result."


# NOT FINISHED
# print("%%% Unit %%%")
# value = getLowestLocation("05-seeds-requirements-list-p1.txt", True)
# Expected = 0
#
# print("The lowest location number is: ", value)
# assert value[0] == Expected, "Not expected result."
