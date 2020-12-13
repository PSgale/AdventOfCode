# Binary space partitioning
import numpy as np


# Function to read data
# Binary space encoded Seats read (your puzzle input).
# Parameters:
# -
# Returns:
# - seat_id_max
# - empty_seat
def load_data(file):
    seat_id_max = 0
    arr = np.zeros(1024)

    with open('../data/' + file, 'r') as f:
        for str in f:
            seat_id = calculate_boarding_pass_id(str.rstrip("\n"))
            arr[seat_id] = 1
            if seat_id > seat_id_max:
                seat_id_max = seat_id
        empty_seat = find_empty_seat(arr)
    return seat_id_max, empty_seat


# Function to calculate Boarding Pass ID
# The first 7 characters will either be F or B;
# these specify exactly one of the 128 rows on the plane (numbered 0 through 127).
# Each letter tells you which half of a region the given seat is in. Start with the whole list of rows;
# the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127).
# The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
# Parameters:
# - char(10) boarding_pass
# Return: (int) Boarding Pass ID
def calculate_boarding_pass_id(boarding_pass):
    fb = boarding_pass[:7]
    fb_binary_id = fb.replace("F", "0").replace("B", "1")
    lr = boarding_pass[-3:]
    lr_binary_id = lr.replace("L", "0").replace("R", "1")
    return int(fb_binary_id, 2) * 8 + int(lr_binary_id, 2)


# Function to determine empty seat after not-available seats
# Return: empty Seat ID
def find_empty_seat(arr):
    if_exist = False
    for i in range(len(arr)):
        if arr[i] == 1:
            if_exist = True
        if arr[i] == 0 and if_exist:
            return i
    return -1


print("%%% Test 1 %%%")
_seat_id_max, _empty_seat = load_data("seat_id1_t1.txt")

Expected = 820
print("Max Seat ID: ", _seat_id_max)
print("Empty Seat ID: ", _empty_seat)
assert _seat_id_max == Expected, "Not expected result."


print("%%% Unit 1 %%%")
_seat_id_max, _empty_seat = load_data("seat_id1.txt")

Expected = [880, 731]
print("Max Seat ID: ", _seat_id_max)
print("Empty Seat ID: ", _empty_seat)
assert [_seat_id_max, _empty_seat] == Expected, "Not expected result."



