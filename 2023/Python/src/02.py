from helpers import readFileLines
import re

CUBES = re.compile(r"(\d+)\s(blue|green|red)")

def isGamePossible(outcomes, initial, isDebug = False):
    for outcome in outcomes.split(";"):

        if isDebug:
            print(outcome)

        cubes = CUBES.findall(outcome)
        for cube_number, cube_color in cubes:
            if (initial[cube_color] < int(cube_number)):
                return False

    return True

def getPossibleGames(file, initial, isDebug = False):
    lines = readFileLines(file)

    total = 0
    for str in lines:
        game_id, outcomes = str.split(":")
        game_id = int(game_id.split(" ")[1])

        if isDebug:
            print(game_id, "--", outcomes)

        if isGamePossible(outcomes, initial, isDebug):
            total += game_id

    return total


print("%%% Test %%%")
initial = {"red": 12, "green": 13, "blue": 14}
value = getPossibleGames("02-cube-game-outcomes-t1.txt", initial, False)

Expected = 8
print("The sum of the IDs of possible games: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
initial = {"red": 12, "green": 13, "blue": 14}
value = getPossibleGames("02-cube-game-outcomes-p1.txt", initial)
print("The sum of the IDs of possible games: ", value)
