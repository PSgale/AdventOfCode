# import rhinoscriptsyntax as rs
from directions import direction_to_instruction


# Make a list of vector coordinates
def combine_path(list):
    i = 1
    path = []
    point = [0, 0, 0]  # 2D point with steps taken to it.
    for move in list:
        instruction = direction_to_instruction.get(move[0:1])
        path_temp, temp = instruction(point, int(move[1:]))

        path.append(path_temp)
        point = temp
    return path


# Function to read memory
def load_paths(file):
    with open('../data/' + file, 'r') as f:
        path_1 = combine_path(f.readline().split(','))
        path_2 = combine_path(f.readline().split(','))
    return path_1, path_2


# Check intersections
# And return Manhattan distance from the central port to the closest intersection
def ger_shortest_distance(path_1, path_2):
    distance = 99999
    length = 99999

    for v1 in path_1:
        for v2 in path_2:

            if v1[0][0] == v1[1][0] and v2[0][1] == v2[1][1]:                                   # case | --
                if v2[0][0] <= v1[0][0] <= v2[1][0] and v1[0][1] <= v2[0][1] <= v1[1][1]:       # intersection
                    if v1[0][1] != 0 and v2[0][0] != 0:
                        distance = abs(v1[0][0]) + abs(v2[0][1]) if 0 < abs(v1[0][0]) + abs(v2[0][1]) <= distance else distance
                        v1_to = v2[0][1] - v1[0][1] if v1[3] == 'o' else v1[1][1] - v2[0][1]
                        v2_to = v1[0][0] - v2[0][0] if v2[3] == 'o' else v2[1][0] - v1[0][0]
                        length = v1[2] + v2[2] + v1_to + v2_to if 0 < v1[2] + v2[2] + v1_to + v2_to <= length else length
                        # print(['case 1', [v1, v2], abs(v1[0][0]) + abs(v2[0][1]), v1[2] + v2[2] + v1_to + v2_to])

            elif v1[0][1] == v1[1][1] and v2[0][0] == v2[1][0]:                                 # case -- |
                if v1[0][0] <= v2[0][0] <= v1[1][0] and v2[0][1] <= v1[0][1] <= v2[1][1]:       # intersection
                    if v1[0][0] != 0 and v2[0][1] != 0:
                        distance = abs(v1[0][1]) + abs(v2[0][0]) if 0 < abs(v1[0][1]) + abs(v2[0][0]) <= distance else distance
                        v1_to = v2[0][0] - v1[0][0] if v1[3] == 'o' else v1[1][0] - v2[0][0]
                        v2_to = v1[0][1] - v2[0][1] if v2[3] == 'o' else v2[1][1] - v1[0][1]
                        length = v1[2] + v2[2] + v1_to + v2_to if 0 < v1[2] + v2[2] + v1_to + v2_to <= length else length
                        # print(['case 2', [v1, v2], abs(v1[0][1]) + abs(v2[0][0]), v1[2] + v2[2] + v1_to + v2_to])

    return distance, length


# Start program

print("%%% Test 1 %%%")
wire_1, wire_2 = load_paths("wires_cross_path_t1.txt")
dist, lng = ger_shortest_distance(wire_1, wire_2)

# Result: Manhattan distance from the central port to the closest intersection
print("Manhattan distance : " + str(dist) + ", Shortest circuit: " + str(lng))
assert dist == 6, "Not expected result."




print("%%% RUN %%%")
wire_1, wire_2 = load_paths("wires_cross_path_1.txt")
dist, lng = ger_shortest_distance(wire_1, wire_2)

# Result:
# Manhattan distance from the central port to the closest intersection
# Shortest path
print("Manhattan distance : " + str(dist) + ", Shortest circuit: " + str(lng))


wire_1, wire_2 = load_paths("wires_cross_path_2.txt")
dist, lng = ger_shortest_distance(wire_1, wire_2)

# Result:
# Manhattan distance from the central port to the closest intersection
# Shortest path
print("Manhattan distance : " + str(dist) + ", Shortest circuit: " + str(lng))