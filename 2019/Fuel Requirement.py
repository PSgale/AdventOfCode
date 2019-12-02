import math


# Function to calculate Fuel
def fuel_required(weight):
    return math.floor(weight / 3) - 2


# Start program
fuel_requirement = 0
f = open("data/fuel_requirements.txt", "r")
for x in f:
    # print(fuel_required(int(x)))
    fuel_requirement = fuel_requirement + fuel_required(int(x))

# Result
print("Total fuel requirement: " + str(fuel_requirement))
