from helpers import readFileLines


def indentifyCard(line, isDebug=False):
    card_id, numbers = line.split(":")
    card_id = int(card_id.replace('Card ', '').strip())

    win = []
    numbers_winning, numbers = numbers.split("|")
    numbers = list(filter(lambda x: (x != ''), numbers.strip().split(" ")))
    numbers_winning = {k: k for k in list(filter(lambda x: (x != ''), numbers_winning.strip().split(" ")))}

    # for val in numbers:
    #     if val in numbers_winning:
    #         win.append(val)
    win.extend(val for val in numbers if val in numbers_winning)

    if isDebug:
        print(card_id, '', numbers_winning, ' <=> ', numbers)
        print(win)

    return [int(card_id), len(win)]


def getNumberOfCards(card, cards, isDebug=False):
    total = 1
    if card[1] == 0:
        return total
    else:
        for card_id in range(card[0] + 1, card[0] + card[1] + 1):
            total += getNumberOfCards([card_id, cards[card_id]], cards, isDebug)
    return total


def getWinningPoints(file, isDebug=False):
    lines = readFileLines(file)
    cards = {}

    total = 0
    for line in lines:
        card_id, wins = indentifyCard(line, isDebug)
        cards[card_id] = wins

    for card_id in cards:
        total += getNumberOfCards([card_id, cards[card_id]], cards, isDebug)

    if isDebug:
        print(cards)

    return total


print("%%% Test %%%")
value = getWinningPoints("04-scratchcards-list-t1.txt", True)

Expected = 30
print("Points cards are worth in total: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = getWinningPoints("04-scratchcards-list-p1.txt")
print("Points cards are worth in total: ", value)
