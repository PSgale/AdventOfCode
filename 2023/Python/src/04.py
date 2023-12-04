from helpers import readFileLines


def indentifyCard(line, isDebug=False):
    card_id, numbers = line.split(":")
    card_id = int(card_id.replace('Card ', '').strip())

    win = []
    numbers_winning, numbers = numbers.split("|")
    numbers = list(filter(lambda x: (x != ''), numbers.strip().split(" ")))
    numbers_winning = {k: k for k in list(filter(lambda x: (x != ''), numbers_winning.strip().split(" ")))}

    for val in numbers:
        if val in numbers_winning:
            win.append(val)

    if isDebug:
        print(card_id, '', numbers_winning, ' <=> ', numbers)
        print(win)

    return [card_id, numbers_winning, numbers, win]


def getWinningPoints(file, isDebug=False):
    lines = readFileLines(file)

    total = 0
    for line in lines:
        card = indentifyCard(line, isDebug)

        if card[3]:
            total += pow(2, len(card[3]) - 1)

            if isDebug:
                print(pow(2, len(card[3])), card[3])

    return total


print("%%% Test %%%")
value = getWinningPoints("04-scratchcards-list-t1.txt", True)

Expected = 13
print("Points cards are worth in total: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = getWinningPoints("04-scratchcards-list-p1.txt")

Expected = 525181
print("Points cards are worth in total: ", value)
assert value == Expected, "Not expected result."
