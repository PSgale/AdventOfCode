from helpers import readFileLines, replaceCharDic
import re

to_replace = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}
def geCalibrationValue(file, isDebug = False):
    lines = readFileLines(file)

    total = 0
    for str in lines:
        str = replaceCharDic(str, to_replace)
        numbers = re.findall(r'\d+', str)
        total += int(numbers[0][0] + numbers[-1][-1])

        if (isDebug):
            print(numbers[0][0], numbers[-1][-1])

    return total


print("%%% Test %%%")
value = geCalibrationValue("01-calibration-document-t2.txt", True)

Expected = 281
print("Calibration value: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = geCalibrationValue("01-calibration-document-p1.txt")
print("Calibration value: ", value)