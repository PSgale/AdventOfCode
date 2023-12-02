from helpers import readFileLines
import numpy
import re

CUBES = re.compile(r"(\d+)\s(blue|green|red)")

def PossibleGame(outcomes, isDebug = False):
    game = {"red": 0, "green": 0, "blue": 0}

    for outcome in outcomes.split(";"):

        if isDebug:
            print(outcome)

        cubes = CUBES.findall(outcome)
        for cube_number, cube_color in cubes:
            if (game[cube_color] < int(cube_number)):
                game[cube_color] = int(cube_number)

    return game

def getPossibleGames(file, isDebug = False):
    lines = readFileLines(file)

    total = 0
    for str in lines:
        game_id, outcomes = str.split(":")
        game_id = int(game_id.split(" ")[1])

        if isDebug:
            print(game_id, "--", outcomes)

        game = PossibleGame(outcomes, isDebug)
        power = numpy.prod(list(game.values()))
        total += power

        if isDebug:
            print(game, power)

    return total


print("%%% Test %%%")
value = getPossibleGames("02-cube-game-outcomes-t1.txt", False)

Expected = 2286
print("The sum of the power of these games: ", value)
assert value == Expected, "Not expected result."


print("%%% Unit %%%")
value = getPossibleGames("02-cube-game-outcomes-p1.txt")

Expected = 69110
print("The sum of the power of these games: ", value)
assert value == Expected, "Not expected result."
