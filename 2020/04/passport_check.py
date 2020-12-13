import re


# Passport records check
# Detect valid passport
# Missing cid is fine, but missing any other field is not.
# Returns:
# - True if all required fields are exists
def f_passport_check_simple(records):
    # records = re.findall(r"[\w-]+:[\w-]+", passport_data)
    required_fields = [["byr", "(Birth Year)"],
                       ["iyr", "(Issue Year)"],
                       ["eyr", "(Expiration Year)"],
                       ["hgt", "(Height)"],
                       ["hcl", "(Hair Color)"],
                       ["ecl", "(Eye Color)"],
                       ["pid", "(Passport ID)"],
                       # ["cid", "(Country ID)"]
                       ]

    for key in required_fields:
        if key[0] not in records:
            # print("Key '" + key[0] + "' does not exists in dictionary: ", records)
            return False
    return True


# Passport records check
# Detect valid passport
# - byr (Birth Year) - four digits; at least 1920 and at most 2002.
# - iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# - eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# - hgt (Height) - a number followed by either cm or in:
#   - If cm, the number must be at least 150 and at most 193.
#   - If in, the number must be at least 59 and at most 76.
# - hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# - ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# - pid (Passport ID) - a nine-digit number, including leading zeroes.
# - cid (Country ID) - ignored, missing or not.
# Missing cid is fine, but missing any other field is not.
# Returns:
# - True if all required fields are exists
def f_passport_check(records):
    # records = re.findall(r"[\w-]+:[\w-]+", passport_data)
    required_fields = [["byr", "(Birth Year)"],
                       ["iyr", "(Issue Year)"],
                       ["eyr", "(Expiration Year)"],
                       ["hgt", "(Height)"],
                       ["hcl", "(Hair Color)"],
                       ["ecl", "(Eye Color)"],
                       ["pid", "(Passport ID)"],
                       # ["cid", "(Country ID)"]
                       ]
    ecl_matches = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    for key in required_fields:
        if key[0] not in records:
            # print("Key '" + key[0] + "' does not exists in dictionary: ", records)
            return False
        else:
            if key[0] == "byr":
                value = re.match(r"^\d{4}$", records[key[0]])
                if not (value and 1920 <= int(value.string) <= 2002):
                    return False
            elif key[0] == "iyr":
                value = re.match(r"^\d{4}$", records[key[0]])
                if not (value and 2010 <= int(value.string) <= 2020):
                    return False
            elif key[0] == "eyr":
                value = re.match(r"^\d{4}$", records[key[0]])
                if not (value and 2020 <= int(value.string) <= 2030):
                    return False
            elif key[0] == "hgt":
                value = re.match(r"^\d+(cm|in)$", records[key[0]])
                if not (value and ((value.string[-2:] == "in" and 59 <= int(value.string[:-2]) <= 76)
                                   or (value.string[-2:] == "cm" and 150 <= int(value.string[:-2]) <= 193))):
                    return False
            elif key[0] == "hcl":
                value = re.match(r"^#[\da-f]{6}$", records[key[0]])
                if not value:
                    return False
            elif key[0] == "ecl":
                if records[key[0]] not in ecl_matches:
                    return False
            elif key[0] == "pid":
                value = re.match(r"^\d{9}$", records[key[0]])
                if not value:
                    return False
    return True