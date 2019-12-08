# Function to read the map
def load_map(file):
    f = open("../data/" + file, "r")

    # load galaxy to dictionary
    map_ = {}
    for x in f:
        key, value = x.strip().split(")")

        values = map_.get(key)
        if values:
            values.append(value)
            map_.update({key: values})
        else:
            map_.update({key: [value]})

    # Check planet not in orbit
    map_copy = map_.copy()
    for values in map_.values():
        for el in values:
            if map_copy.get(el):
                map_copy.pop(el)

    return map_, [*map_copy]

# calculate orbits in galaxy
def calculate_orbits_check_sum(map_, planet, orbits):
    if map_.get(planet):
        return orbits + sum(calculate_orbits_check_sum(map_, planet_on_orbit, orbits + 1) for planet_on_orbit in map_.get(planet))
    else:
        return orbits


def get_dist_to_santa(map_):
    map_rev = {}
    for planet in map_:
        for orbit in map_.get(planet):
            map_rev.update({orbit: planet})

    # SAN path to COM
    dict_san = {}
    planet_now = 'SAN'
    dist = 1
    while planet_now:
        planet_now = map_rev.get(planet_now)
        if planet_now:
            dict_san.update({planet_now: dist})
            dist += 1

    # YOU path to COM
    dict_you = {}
    planet_now = 'YOU'
    dist = 1
    while planet_now:
        planet_now = map_rev.get(planet_now)
        if planet_now:
            dict_you.update({planet_now: dist})
            dist += 1

    # Find common path and distance between
    dict_common = dict_san.keys() & dict_you.keys()
    min_path = 99999
    for planet in dict_common:
        path_ = dict_san.get(planet) + dict_you.get(planet)
        min_path = path_ if path_ < min_path else min_path

    return min_path - 2


print("%%% Test 1 %%%")
map_, no_orbit = load_map("number_of_orbits_t1.txt")
orbits_check_sum = calculate_orbits_check_sum(map_, no_orbit[0], 0)

expected = 42
assert orbits_check_sum == expected, "Not expected result."


print("%%% Test 2 %%%")
map_, no_orbit = load_map("number_of_orbits_t2.txt")

orbits_check_sum = calculate_orbits_check_sum(map_, no_orbit[0], 0)
expected = 54
assert orbits_check_sum == expected, "Not expected result."

dist_to_santa = get_dist_to_santa(map_)
expected = 4
assert dist_to_santa == expected, "Not expected result."




print("%%% RUN %%%")
map_, no_orbit = load_map("number_of_orbits.txt")
orbits_check_sum = calculate_orbits_check_sum(map_, no_orbit[0], 0)

print('No orbit' + str(no_orbit))

expected = 106065
assert orbits_check_sum == expected, "Not expected result."

dist_to_santa = get_dist_to_santa(map_)
print(dist_to_santa)


