import numpy as np


# Function to check password criteria:
# 1. Two adjacent digits are the same
# 2. Digits are never decrease
def check_main_criteria(number):
    numbers_ = np.asarray([int(char) for char in str(number)])
    _numbers = numbers_[1:]
    numbers_ = numbers_[:-1]

    if all([x >= 0 for x in _numbers - numbers_]) and \
            any([x == 0 for x in _numbers - numbers_]):
        return True
    return False


# Function to check password criteria:
# 1. The two adjacent matching digits are not part of a larger group of matching digits
def check_last_criteria(number):
    numbers_ = np.asarray([int(char) for char in str(number)])
    _numbers = numbers_[1:]
    numbers_ = numbers_[:-1]

    snumber = ''.join(['1' if x == 0 else '0' for x in _numbers - numbers_])
    if snumber[:2] == '10' or snumber[-2:] == '01' or \
            '010' in snumber:
        return True
    return False


print("%%% RUN %%%")
first_number = 134792
last_number = 675810
number_of_passwords = 0
number_of_passwords_2 = 0

for current in range(first_number, last_number):
    if check_main_criteria(current):
        number_of_passwords += 1
        # print(current)
        if check_last_criteria(current):
            number_of_passwords_2 += 1
            # print(current)

print("Number of passwords: " + str(number_of_passwords))
print("Number of passwords with last criteria: " + str(number_of_passwords_2))



# Check new groupby feature
# returns dataset: distinct char value and group of same chars
# from itertools import groupby
# block_length = [len(list(g)) for _, g in groupby(str(n))]