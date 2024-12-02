from helpers import readFileLines, excludeElement

# Check if Report is safe
def checkIfSafe(report, isDebug = False):

    isIncreasing = 0
    isDecreasing = 0

    for i in range(1, len(report)):
        if report[i] > report[i - 1] > 0:
            isIncreasing = 1
        else:
            isDecreasing = 1

        # False if rules not satisfy:
        # 1. The levels are either all increasing or all decreasing.
        # 2. Any two adjacent levels differ by at least one and at most three.
        if isDecreasing == isIncreasing or report[i - 1] == report[i] or abs(report[i - 1] - report[i]) > 3:
            return [False, i]

    return [True, 0]

def getSafeReportsNumber(file, tolerance_level, isDebug = False):
    lines = readFileLines(file)

    total_safe = 0
    # Load data
    for str in lines:
        numbers = [int(x) for x in str.split(' ')]

        if isDebug:
            print(numbers)

        isSafe = False
        wrongLevel = 0
        tolerance = tolerance_level
        while (tolerance > 0):
            if wrongLevel > 0:
                wrongLevel_ = wrongLevel

                # On level 2, first level can be skipped and has to be checked separately
                if not isSafe and wrongLevel_ == 2:
                    if isDebug:
                        print("numers_fixed L", excludeElement(numbers, 0))

                    isSafe, wrongLevel = checkIfSafe(excludeElement(numbers, 0), isDebug)

                if not isSafe:
                    if isDebug:
                        print("numers_fixed O", excludeElement(numbers, wrongLevel_-1))

                    isSafe, wrongLevel = checkIfSafe(excludeElement(numbers, wrongLevel_-1), isDebug)

                if not isSafe:
                    if isDebug:
                        print("numers_fixed R", excludeElement(numbers, wrongLevel_))

                    isSafe, wrongLevel = checkIfSafe(excludeElement(numbers, wrongLevel_), isDebug)
            else:
                isSafe, wrongLevel = checkIfSafe(numbers, isDebug)

            if isDebug:
                if isSafe:
                    print(f"Tolerance: {tolerance}, is safe {isSafe}")
                else:
                    print(f"Tolerance: {tolerance}, is safe {isSafe}, wrong level {wrongLevel} - {numbers[wrongLevel-1]}")

            if isSafe:
                break

            tolerance -= 1

        if isSafe:
            total_safe += 1

            if isDebug:
                print("Report is safe")

    return total_safe


print("%%% Test 1 %%%")
value1 = getSafeReportsNumber("02-reports-levels-t1.txt", 1, True)

Expected = 2
print("#Safe reports: ", value1)
assert value1 == Expected, "Not expected result."

print("%%% Test 2 %%%")
value1 = getSafeReportsNumber("02-reports-levels-t1.txt", 2, True)

Expected = 4
print("#Safe reports: ", value1)
assert value1 == Expected, "Not expected result."


print("%%% Unit 1 %%%")
value1 = getSafeReportsNumber("02-reports-levels-p1.txt", 1)
print("#Safe reports: ", value1)

print("%%% Unit 2 %%%")
value1 = getSafeReportsNumber("02-reports-levels-p1.txt", 2)
print("#Safe reports: ", value1)