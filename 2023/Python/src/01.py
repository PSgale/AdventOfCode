from helpers import readFileLines
import re

def geCalibrationValue(file, isDebug = False):
    lines = readFileLines(file)

    total = 0
    for str in lines:
        numbers = re.findall(r'\d+', str)
        total += int(numbers[0][0] + numbers[-1][-1])

        if (isDebug):
            print(numbers[0][0], numbers[-1][-1])

    return total


print("%%% Test %%%")
value = geCalibrationValue("01-calibration-document-t1.txt", True)

Expected = 142
print("Calibration value: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = geCalibrationValue("01-calibration-document-p1.txt")
print("Calibration value: ", value)