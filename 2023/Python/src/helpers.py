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
