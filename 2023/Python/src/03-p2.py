from helpers import readFileLines
from itertools import groupby
import re

SYMBOL = re.compile(r"([^\w.\n])")
NUMBER = re.compile(r"(\d+)")


def identifySymbols(lines, isDebug=False):
    symbols_dict = {}

    i_symbols = 0
    for line in lines:
        symbols = SYMBOL.search(line)
        symbols_list = []

        while symbols:
            symbols_list.append([symbols.span()[0], symbols.group()])
            symbols = SYMBOL.search(line, symbols.span()[1])

        if symbols_list:
            symbols_dict[i_symbols] = symbols_list

            if isDebug:
                print('Symbols in row', i_symbols, ':', symbols_list)

        i_symbols += 1

    return symbols_dict


def identifyEngineParts(lines, symbols_dict, isDebug=False):
    gearParts_list = []

    i_numbers = 0
    for line in lines:
        numbers = NUMBER.search(line)

        while numbers:
            gearPart = getGearPart(numbers, i_numbers, symbols_dict, isDebug)
            if gearPart:
                gearParts_list.append(gearPart)
            numbers = NUMBER.search(line, numbers.span()[1])

        i_numbers += 1

    return gearParts_list


def getGearPart(number_match, i_numbers, symbols_dict, isDebug=False):
    # all indexes starts from 0
    # Filter by row
    for i in range(i_numbers - 1, i_numbers + 2):
        if i in symbols_dict:
            for symbol in symbols_dict[i]:

                if isDebug:
                    print(number_match, i_numbers, symbols_dict[i])
                    print(number_match.group(), '<=>', symbol[1], ':',
                          symbol[0], '>=', number_match.span()[0] - 1, 'and', symbol[0], '<=', number_match.span()[1],
                          number_match.span()[0] - 1 <= symbol[0] <= number_match.span()[1])
                # Filter by column
                if number_match.span()[0] - 1 <= symbol[0] <= number_match.span()[1] and symbol[1] == '*':
                    return [str(i) + '_' + str(symbol[0]), int(number_match.group())]

    return []


def getGearRatiosHash(file, isDebug=False):
    lines = readFileLines(file)
    total = 0

    symbols_dict = identifySymbols(lines, isDebug)
    gearParts_list = identifyEngineParts(lines, symbols_dict, isDebug)

    if isDebug:
        print(symbols_dict)
        print(gearParts_list)

    # use first element for grouping
    gearParts_grouped = [list(v) for _, v in groupby(sorted(gearParts_list, key=lambda x: x[0]), lambda x: x[0])]
    for gearParts_group in gearParts_grouped:
        if len(gearParts_group) == 2:
            total += gearParts_group[0][1] * gearParts_group[1][1]

    if isDebug:
        print('Gear parts grouped:', gearParts_grouped)
        print(total)

    # reduce(lambda a, b: a + b, engineParts_list)
    return total


print("%%% Test %%%")
value = getGearRatiosHash("03-engine-part-numbers-t1.txt", False)

Expected = 467835
print("the sum of all the gear ratios in your engine schematic: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = getGearRatiosHash("03-engine-part-numbers-p1.txt")

Expected = 84289137
print("the sum of all of the gear ratios in your engine schematic: ", value)
assert value == Expected, "Not expected result."
