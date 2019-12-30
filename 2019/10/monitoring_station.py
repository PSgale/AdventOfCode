import pandas as pd
import math


# Function to read asteroid map
def read_map(file):
    nrow = 0
    map = []
    with open('../data/' + file, 'r') as f:
        for row in f:
            ncol = 0
            for el in list(row):
                if el == '#':
                    map.append((ncol, nrow))

                ncol += 1
            nrow += 1
    return map


# Process asteroid map to find the best candidate for monitoring station
def process_map(map):
    max_asteroids = 0
    max_visible = {}
    from_asteroid = (0, 0)

    for ast0 in map:

        visible = {}
        for ast1 in map:
            if ast0 == ast1:
                continue

            x = ast1[0] - ast0[0]
            y = ast1[1] - ast0[1]

            if x == 0:
                k = 9999
            elif y == 0:
                k = -9999
            else:
                k = y / x

            if y >= 0 and x > 0:        # y > 0 and x >= 0:
                d = 'ES'
                initial_degree = 90
                side = abs(x)
            elif y > 0 and x <= 0:      # y >= 0 and x < 0:
                d = 'WS'
                initial_degree = 180
                side = abs(y)
            elif y < 0 and x >= 0:      # y <= 0 and x > 0:
                d = 'NE'
                initial_degree = 0
                side = abs(y)
            else:
                d = 'NW'
                initial_degree = 270
                side = abs(x)

            hyp = math.sqrt(x * x + y * y)

            # There are two methods how to represent the angle. Use one.
            # 1. angle in degrees
            # 2. direction and coefficient
            view = initial_degree + round(math.degrees(math.acos(side / hyp)), 2)
            # view = (k, d)

            # Add position if asteroid is new in that angle
            # if not visible.get(view):
            asteroids = visible.get(view)
            if asteroids is None:
                asteroids = [ast1]
            else:
                asteroids.append(ast1)
            # asteroids.sort()
            asteroids = sorted(asteroids, key=lambda asteroid: abs(asteroid[0] - ast0[0]) + abs(asteroid[1] - ast0[1]))
            visible.update({view: asteroids})

        # Compare visible asteroids
        if max_asteroids < len(visible.items()):
            max_asteroids   = len(visible.items())
            max_visible     = visible
            from_asteroid   = ast0
            # print("From Asteroid : " + str(from_asteroid) + " Max Asteroids : " + str(max_asteroids) + " Visible : " + str(visible))

    return max_asteroids, from_asteroid, max_visible


def print_map(map, vaporized):
    x = 0
    y = 0
    map_dict = {}

    # Detect borders
    for el in map:
        if x < el[0]:
            x = el[0]
        if y < el[1]:
            y = el[1]
        map_dict.update({el: 0})

    # Print map
    for j in range(y + 1):
        map_row = ''
        for i in range(x + 1):
            if map_dict.get((i, j)) is None:
                map_row += '.'
            else:
                order = vaporized.get((i, j))
                if order is None:
                    map_row += '#'
                else:
                    map_row += str(order)
        print(map_row)


# vaporise number of asteroids
def vaporize(visible, to_vaporize):
    directions = [key for key in visible.keys()]
    directions.sort()

    vaporized = {}
    rotation = 0
    order = 1
    while to_vaporize > 0:
        for d in directions:
            targeted = visible.get(d)
            if len(targeted) > rotation:
                vaporized.update({targeted[rotation]: order})
                to_vaporize -= 1
                order += 1
            if to_vaporize == 0:
                break
        rotation += 1


    return vaporized





# Start program

print("%%% Test 1 %%%")
Map = read_map("monitoring_station_t1.txt")
Max_Asteroids, From_Asteroid, Max_Visible = process_map(Map)

print("From Asteroid : " + str(From_Asteroid) + " Max Asteroids : " + str(Max_Asteroids))
Expected = 8
assert Max_Asteroids == Expected, "Not expected result."



print("%%% Test 2 %%%")
Map = read_map("monitoring_station_t2.txt")
Max_Asteroids, From_Asteroid, Max_Visible = process_map(Map)

print("From Asteroid : " + str(From_Asteroid) + " Max Asteroids : " + str(Max_Asteroids))
Expected = 210
assert Max_Asteroids == Expected, "Not expected result."

# df = pd.DataFrame(list(Max_Visible.keys()), columns=['k', 'direction', 'angle'])
# print(df.head())
# print(df['angle'].value_counts().head())
# print(df[df['angle'] == 90])

# for key in Max_Visible.keys():
#     if key[2] == 90:
#         print(key)
#         print(Max_Visible.get(key))



print("%%% Test 3 %%%")
Map = read_map("monitoring_station_t3.txt")
Max_Asteroids, From_Asteroid, Max_Visible = process_map(Map)
Vaporized = vaporize(Max_Visible, 9)
print_map(Map, Vaporized)

# print(Vaporized)

print("From Asteroid : " + str(From_Asteroid) + " Max Asteroids : " + str(Max_Asteroids))
Expected = 210
# assert Max_Asteroids == Expected, "Not expected result."



print("%%% Test 4 %%%")
Map = read_map("monitoring_station_t1.txt")
Max_Asteroids, From_Asteroid, Max_Visible = process_map(Map)
Vaporized = vaporize(Max_Visible, 8)
print_map(Map, Vaporized)

# print(Max_Visible)
# print(Vaporized)

print("From Asteroid : " + str(From_Asteroid) + " Max Asteroids : " + str(Max_Asteroids))



print("%%% RUN %%%")
# 1.
Map = read_map("monitoring_station.txt")
Max_Asteroids, From_Asteroid, Max_Visible = process_map(Map)

Expected = 276
print("From Asteroid : " + str(From_Asteroid) + " Max Asteroids : " + str(Max_Asteroids))

# 2.
Vaporized = vaporize(Max_Visible, 201)
# print_map(Map, Vaporized)

print(Vaporized)