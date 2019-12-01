import math


def fuel_required(weight):
    return math.floor(weight / 3) - 2


fuel_requirement = 0
f = open("data/fuel_requirements.txt", "r")
for x in f:
    # print(fuel_required(int(x)))
    fuel_requirement = fuel_requirement + fuel_required(int(x))

print("Total fuel requirement: " + str(fuel_requirement))
