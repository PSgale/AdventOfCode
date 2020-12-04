# Read list of numbers, find the two entries that sum to 2020 and then multiply those two numbers together.


# Function to read data
def load_paths(file):
    _report = []
    with open('../data/' + file, 'r') as f:
        _report = [int(i) for i in f]
    return _report


# Function to find indexes of 2 numbers which sum to 2020
# Returns: numbers indexes
def sum2_to_2020(_report):
    # First number
    for i in range(len(_report)):
        # Second number
        for j in range(i+1, len(_report)):
            if _report[i] + _report[j] > 2020:
                break
            elif _report[i] + _report[j] == 2020:
                return i, j
            else:
                # _report[i] + _report[j] < 2020:
                continue


# Function to find indexes of 3 numbers which sum to 2020
# Returns: numbers indexes
def sum3_to_2020(_report):
    # First number
    for i in range(len(_report)):
        # Second number
        for j in range(i + 1, len(_report)):
            # Third number
            for k in range(j + 1, len(_report)):
                if _report[i] + _report[j] + _report[k] > 2020:
                    break
                elif _report[i] + _report[j] + _report[k] == 2020:
                    return i, j, k
                else:
                    # _report[i] + _report[j] < 2020:
                    continue


report = load_paths("expense_report.txt")
report_sorted = sorted(report)
# print(report)

print("%%% Test 1 %%%")
index1, index2 = sum2_to_2020(report_sorted)

Expected = 2020
assert report_sorted[index1] + report_sorted[index2] == Expected, "Not expected result."
print("Numbers are: ", report_sorted[index1], report_sorted[index2])
print("Multiply them: ", report_sorted[index1] * report_sorted[index2])



print("%%% Test 2 %%%")
index1, index2, index3 = sum3_to_2020(report_sorted)

Expected = 2020
assert report_sorted[index1] + report_sorted[index2] + report_sorted[index3] == Expected, "Not expected result."
print("Numbers are: ", report_sorted[index1], report_sorted[index2], report_sorted[index3])
print("Multiply them: ", report_sorted[index1] * report_sorted[index2] * report_sorted[index3])