# Find which angles will take you near the fewest trees.
import numpy as np


# Function to read data
# Parameters:
# - point - Matrix with initial positions
# - move - Matrix with move
# Returns: Vector of Trees found
def load_data(file, move, point):
    row_num = 1
    tree_num = np.zeros(move.shape[0], dtype=np.int64)

    with open('../data/' + file, 'r') as f:
        for str in f:
            point, tree_num = move_toboggan(str, row_num, move, point, tree_num)
            row_num += 1

    return tree_num


# Move Toboggan
# Due to the local geology, trees in this area only grow on exact integer coordinates in a grid.
# You make a map (your puzzle input) of the open squares (.) and trees (#) you can see.
# Returns:
# - Matrix with new positions
# - Vector of Trees found
def move_toboggan(line, row_num, move, point, tree_num):

    for i in range(move.shape[0]):
        if row_num == point[i, 0]:
            if line[point[i, 1]-1:point[i, 1]] == "#":
                tree_num[i] += 1
                # print(line[0:point[1] - 1] + "X" + line[point[1]:len(line)], "at (", point[0], ", ", point[1], ")")

            # set new point
            point[i, 0] = point[i, 0] + move[i, 0]
            point[i, 1] = point[i, 1] + move[i, 1]

            # Find position on map if cross the border
            if len(line) <= point[i, 1]:
                point[i, 1] = point[i, 1] - len(line) + 1

    return point, tree_num


print("%%% Test 1 %%%")
_move = np.array([[1, 3]])
_point = np.ones(_move.shape, dtype=np.int16)
_tree_num = load_data("toboggan_trajektory1_t1.txt", _move, _point)

Expected = 7
print("Trees found: ", _tree_num)
assert _tree_num[0] == Expected, "Not expected result."


print("%%% Unit 1 %%%")
_move = np.array([[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]])
_point = np.ones(_move.shape, dtype=np.int16)
_tree_num = load_data("toboggan_trajektory.txt", _move, _point)

Expected = 280
print("Trees found: ", _tree_num)
assert _tree_num[1] == Expected, "Not expected result."


print("%%% Unit 2 %%%")
mult = np.prod(_tree_num)

Expected = 4355551200
print("Multiplication the number of trees: ", mult)
# assert _tree_num[1] == Expected, "Not expected result."

