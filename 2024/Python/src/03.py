from helpers import readFileLines, replaceCharDic
import re

char_map = {"o": "", "n": "", "mul(": "o", ")": "n"}

def doInstructions(file, useDoRule = False, isDebug = False):
    lines = readFileLines(file)
    line = "".join(lines)

    if useDoRule:
        # Apply do rule
        # do() - start processing
        # don't() - stop processing
        line = "".join([do.split("don't()")[0] for do in line.split("do()")])
        if isDebug:
            print("Do rule applied")

    line_cleaned = replaceCharDic(line, char_map)
    instructions = re.findall(r'o\d+,\d+n', line_cleaned)
    operands = [[int(x) for x in str.replace('o','').replace('n', '').split(',')] for str in instructions]

    total_result = 0
    for x, y in operands:
        total_result += x * y

    if isDebug:
        print(operands)

    return total_result


print("%%% Test 1 %%%")
value1 = doInstructions("03-mul-instructions-t1.txt", True, True)

Expected = 161
print("Total result: ", value1)
assert value1 == Expected, "Not expected result."


print("%%% Test 2 %%%")
value1 = doInstructions("03-mul-instructions-t2.txt", True, True)

Expected = 48
print("Total result: ", value1)
assert value1 == Expected, "Not expected result."


print("%%% Unit 1 %%%")
value1 = doInstructions("03-mul-instructions-p1.txt")

Expected = 192767529
print("Total result: ", value1)
assert value1 == Expected, "Not expected result."


print("%%% Unit 2 %%%")
value1 = doInstructions("03-mul-instructions-p1.txt", True)

Expected = 104083373
print("Total result: ", value1)
assert value1 == Expected, "Not expected result."
