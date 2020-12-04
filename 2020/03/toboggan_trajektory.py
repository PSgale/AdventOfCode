# Find which angles will take you near the fewest trees.


# Function to read data
# Returns: Trees found
def load_data(file):
    row_num = 1
    tree_num = 0

    with open('../data/' + file, 'r') as f:
        for str in f:
            if move_toboggan(str, row_num):
                tree_num += 1
            row_num += 1

    return tree_num


# Move Toboggan
# Returns: True if tree
# Due to the local geology, trees in this area only grow on exact integer coordinates in a grid.
# You make a map (your puzzle input) of the open squares (.) and trees (#) you can see.
def move_toboggan(line, row_num):
    tree_exists = False

    if row_num == point[0]:
        if line[point[1]-1:point[1]] == "#":
            tree_exists = True
            # print("At (", point[0], ", ", point[1], ")", line[point[1]-1:point[1]], "   ", line[0:point[1]-1], "O", line[point[1]:len(line)])

        # set new point
        point[0] = point[0] + move[0]
        point[1] = point[1] + move[1]

        # Find position on map if cross the border
        if len(line) < point[1]:
            point[1] = point[1] - len(line) + 1

    return tree_exists


print("%%% Test 1 %%%")
point = [1, 1]
move = [1, 3]
_tree_num = load_data("toboggan_trajektory1_t1.txt")

Expected = 7
assert _tree_num == Expected, "Not expected result."
print("Trees found: ", _tree_num)



print("%%% Test 2 %%%")
point = [1, 1]
move = [1, 3]
_tree_num = load_data("toboggan_trajektory.txt")

Expected = 274
assert _tree_num == Expected, "Not expected result."
print("Trees found: ", _tree_num)
