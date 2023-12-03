from helpers import readFileLines
from functools import reduce
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
    engineParts_list = []

    i_numbers = 0
    for line in lines:
        numbers = NUMBER.search(line)

        while numbers:
            if isEnginePart(numbers, i_numbers, symbols_dict, isDebug):
                engineParts_list.append(int(numbers.group()))
            numbers = NUMBER.search(line, numbers.span()[1])

        i_numbers += 1

    return engineParts_list


def isEnginePart(number_match, i_numbers, symbols_dict, isDebug=False):
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
                if number_match.span()[0] - 1 <= symbol[0] <= number_match.span()[1]:
                    return True

    return False


def getEnginePartsHash(file, isDebug=False):
    lines = readFileLines(file)
    symbols_dict = identifySymbols(lines, isDebug)
    engineParts_list = identifyEngineParts(lines, symbols_dict, isDebug)

    if isDebug:
        print(symbols_dict)
        print(engineParts_list)

    return reduce(lambda a, b: a + b, engineParts_list)


print("%%% Test %%%")
value = getEnginePartsHash("03-engine-part-numbers-t1.txt", False)

Expected = 4361
print("The sum of all the part numbers in the engine schematic: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = getEnginePartsHash("03-engine-part-numbers-p1.txt")

Expected = 525181
print("The sum of all the part numbers in the engine schematic: ", value)
assert value == Expected, "Not expected result."
