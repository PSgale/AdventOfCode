# Functions return path and point.
# Path has smaller point first always.
def Up(point, move):
    return [[point[0], point[1]], [point[0], point[1] + move], point[2], 'o'], \
           [point[0], point[1] + move, point[2] + move, point[2] + move]


def Down(point, move):
    return [[point[0], point[1] - move], [point[0], point[1]], point[2], '-'], \
           [point[0], point[1] - move, point[2] + move]


def Left(point, move):
    return [[point[0] - move, point[1]], [point[0], point[1]], point[2], '-'], \
           [point[0] - move, point[1], point[2] + move]


def Right(point, move):
    return [[point[0], point[1]], [point[0] + move, point[1]], point[2], 'o'], \
           [point[0] + move, point[1], point[2] + move]


# opcode -> (function, number of parameters)
direction_to_instruction = {
    'U': Up,
    'D': Down,
    'L': Left,
    'R': Right
}