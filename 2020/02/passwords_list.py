# Identify how many passwords are valid according to their policies.


# Function to read data
# Row format: "5-10 b: bhbjlkbbbbbbb"
def load_data(file):
    n1 = 0
    n2 = 0

    with open('../data/' + file, 'r') as f:
        for str in f:
            temp, password = str.split(":")
            temp, char = temp.split(" ")
            dig1, dig2 = temp.split("-")

            if check_password1(int(dig1), int(dig2), char, password):
                n1 += 1

            if check_password2(int(dig1), int(dig2), char, password):
                n2 += 1

    return n1, n2


# Function to test password
# Returns: True - if password is correct
# The password policy indicates the lowest and highest number of times
# a given letter must appear for the password to be valid.
# For example, "1-3 a" means that the password must contain "a" at least 1 time and at most 3 times.
def check_password1(dig1, dig2, char, password):
    if dig1 <= password.count(char) <= dig2:
        return True
    else:
        # print(dig1, dig2, "---", char, "---", password)
        return False


# Function to test password
# Returns: True - if password is correct
# Each policy actually describes two positions in the password, where
# 1 means the first character, 2 means the second character, and so on.
# Exactly one of these positions must contain the given letter.
def check_password2(dig1, dig2, char, password):
    if bool(password[dig1:dig1+1] == char) ^ bool(password[dig2:dig2+1] == char):
        # print(dig1, dig2, "---", char, "---", password)
        return True
    else:
        # print(dig1, dig2, "---", char, "---", password)
        return False


NbrGoodPsw1, NbrGoodPsw2  = load_data("passwords_list.txt")


print("%%% Test 1 %%%")

Expected = 439
assert NbrGoodPsw1 == Expected, "Not expected result."
print("Number of Correct Passwords is: ", NbrGoodPsw1)


print("%%% Test 2 %%%")

Expected = 584
assert NbrGoodPsw2 == Expected, "Not expected result."
print("Number of Correct Passwords is: ", NbrGoodPsw2)
