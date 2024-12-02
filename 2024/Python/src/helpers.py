# Function to read data
def readFileLines(file):
    _lines = []

    with open('../data/' + file, 'r') as f:
        _lines = [i.strip() for i in f]

    return _lines


def replaceCharDic(line, to_replace):
    # to_replace - dictionary for character to replace
    for char in to_replace.keys():
        line = line.replace(char, to_replace[char])

    return line

# Exclude element from a list by index
def excludeElement(numbers, exclude_index):
    output = []
    for index, item in enumerate(numbers):
        if index == exclude_index:
            continue
        output.append(item)
    return output

# Greatest Common Divisor (GCD)
# The GCD of two or more integers is the largest integer that divides each of the integers
def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)

    return gcd(a % b, b) if a > b else gcd(a, b % a)


# Least Common Multiple (LCM)
# The LCM is the smallest number that is divisible by all given numbers
def lcm(a, b):
    return int(a * b / gcd(a, b))
