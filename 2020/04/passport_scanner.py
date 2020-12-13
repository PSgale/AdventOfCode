# Detect which passports have all required fields.
from passport_check import f_passport_check, f_passport_check_simple


# Function to read data
# Passport data is validated in batch files (your puzzle input).
# Passports are separated by blank lines.
# Parameters:
# -
# Returns:
def load_data(file):
    valid_passports = 0
    valid_passports_simple = 0
    passport_data = ""

    with open('../data/' + file, 'r') as f:
        for str in f:
            if str == "\n":
                # print(passport_data)
                records = passport_scanner(passport_data.lstrip())
                if f_passport_check_simple(records):
                    valid_passports_simple += 1
                if f_passport_check(records):
                    valid_passports += 1
                passport_data = ""
            else:
                passport_data = passport_data + " " + str.rstrip("\n")

    return valid_passports, valid_passports_simple


# Passport Scanner
# Each passport is represented as a sequence of key:value pairs separated by spaces or newlines.
# Missing cid is fine, but missing any other field is not.
# Returns:
# - Dictionary of passport fields
def passport_scanner(passport_data):
    # records = re.findall(r"[\w-]+:[\w-]+", passport_data)
    records = {tuple[0]: tuple[1]
               for tuple in [record.split(":")
                             for record in passport_data.split(" ")]}

    # print(records)
    return records


print("%%% Test 1 %%%")
_, _valid_passports = load_data("passports_data1_t1.txt")

Expected = 2
print("Valid Passports found: ", _valid_passports)
assert _valid_passports == Expected, "Not expected result."


print("%%% Test 2 %%%")
_valid_passports, _valid_passports_simple = load_data("passports_data2_t1.txt")

Expected = 4
print("Valid Passports found: ", _valid_passports)
assert _valid_passports == Expected, "Not expected result."


print("%%% Unit 1 %%%")
_valid_passports, _valid_passports_simple = load_data("passports_data1.txt")

Expected = 233
print("Valid Passports found: ", _valid_passports_simple)
assert _valid_passports_simple == Expected, "Not expected result."


print("%%% Unit 2 %%%")
Expected = 111
print("Valid Passports found: ", _valid_passports)
assert _valid_passports == Expected, "Not expected result."
