from helpers import readFileLines, replaceCharDic
from itertools import groupby

# Ordered to not replace mapped values
card_map = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "A": "E", "K": "D", "Q": "C", "J": "B", "T": "A"}


def getHandStrength(cards, isDebug=False):
    hand = replaceCharDic(cards, card_map)

    hand_freq = sorted([len(list(group)) for key, group in groupby(sorted([x for x in cards]))], key=None, reverse=True)
    if hand_freq[0] == 5:
        hand_type = 'Five of a kind'
        hand_value = '9'
    elif hand_freq[0] == 4:
        hand_type = 'Four of a kind'
        hand_value = '8'
    elif hand_freq[0] == 3 and hand_freq[1] == 2:
        hand_type = 'Full house'
        hand_value = '7'
    elif hand_freq[0] == 3:
        hand_type = 'Three of a kind'
        hand_value = '6'
    elif hand_freq[0] == 2 and hand_freq[1] == 2:
        hand_type = 'Two pair'
        hand_value = '5'
    elif hand_freq[0] == 2:
        hand_type = 'One pair'
        hand_value = '4'
    elif hand_freq[0] == 1:
        hand_type = 'High card'
        hand_value = '3'
    else:
        hand_type = 'Other cards'
        hand_value = '1'

    if isDebug:
        print(cards, hand_value, hand_type, hand, sorted([x for x in cards]))

    return int(hand_value + hand, 16)


def getWinningOptionsHash(file, isDebug=False):
    lines = readFileLines(file)
    hands = []

    for line in lines:
        cards, bid = (' '.join(line.split()).split(' '))
        hands.append([getHandStrength(cards, isDebug), cards, int(bid)])

    total = 0
    hands.sort(key=lambda x: x[0])
    for idx, val in enumerate(hands):
        total += (idx + 1) * val[2]

    if isDebug:
        print(hands)

    return total


print("%%% Test %%%")
value = getWinningOptionsHash("07-camel-cards-list-t1.txt", True)

Expected = 6440
print("Total winnings: ", value)
assert value == Expected, "Not expected result."

print("%%% Unit %%%")
value = getWinningOptionsHash("07-camel-cards-list-p1.txt")
print("Total winnings: ", value)
