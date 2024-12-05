from helpers import readFileLines
from collections import Counter
import re

# Get first word symbol positions in text
def get_start_points(lines, word, isDebug):
  symbol = re.compile(word[0])

  # Collect words starting positions
  start_points = []
  for i, line in enumerate(lines):
    next_location = symbol.search(line)
    while next_location:
      start_points.append([i, next_location.span()[0]])
      next_location = symbol.search(line, next_location.span()[1])

  if isDebug:
    print(start_points)

  return start_points

# Identify word locations and calculate count of word and word_x
def searchWord(word, directions, lines, start_points, isDebug = False):

  if isDebug:
    print(f"Space size is {[len(lines), len(lines[0])]}")

  list_a_locations = []
  word_total = 0
  for point in start_points:
    for direction in directions:
      i, j = point

      if isDebug:
        print(f"Word {word} from point {[i, j]} in direction {direction}")

      # Check border
      if      i + (len(word) - 1) * direction[0] > len(lines) - 1     \
          or  i + (len(word) - 1) * direction[0] < 0                  \
          or  j + (len(word) - 1) * direction[1] > len(lines[0]) - 1  \
          or  j + (len(word) - 1) * direction[1] < 0:

        if isDebug:
          print(f"Expected position of last symbol {[i + (len(word) - 1) * direction[0], j + (len(word) - 1) * direction[1]]}")
          print(f"Word {word} pass the border")
        continue

      else:
        a_location = ""
        # Check every word letter in the text
        for l in range(len(word) - 1):
          i, j = i + direction[0], j + direction[1]
          if isDebug:
            print(f"{[i,j]} {lines[i][j]} == {word[l+1]}")

          if word[l+1] == "A":
            a_location = f"{i}_{j}"

          if lines[i][j] != word[l+1]:
            break

          if l + 1 == len(word) - 1:
            word_total += 1
            list_a_locations.append(a_location)

  word_x_total = 0
  # Calculate frequency of elements in list list_a_locations
  a_locations_to_frequencies = Counter(list_a_locations)
  for key in a_locations_to_frequencies:
    # Checking number of word intersections
    if a_locations_to_frequencies[key] > 1:
      word_x_total += 1

  if isDebug:
    print(list_a_locations)
    print(a_locations_to_frequencies)
    print(f"Word {word} intersections: {word_x_total}")

  return word_total, word_x_total

def doWordSearch(file, word, directions, isDebug = False):
  lines = readFileLines(file)

  if isDebug:
    print(lines)

  start_points = get_start_points(lines, word, isDebug)
  word_total, word_x_total = searchWord(word, directions, lines, start_points, isDebug)

  return word_total, word_x_total


print("%%% Test 1 %%%")
word_directions = [[1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0]]
word_to_search = "XMAS"
value1, _ = doWordSearch("04-word-search-t1.txt", word_to_search, word_directions,True)

Expected = 4
print("Total result: ", value1)
assert value1 == Expected, "Not expected result."


print("%%% Test 2 %%%")
word_directions = [[1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0]]
word_to_search = "XMAS"
value1, _ = doWordSearch("04-word-search-t2.txt", word_to_search, word_directions, True)

Expected = 18
print("Total result: ", value1)
assert value1 == Expected, "Not expected result."


print("%%% Test 3 %%%")
word_directions = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
word_to_search = "MAS"
value1, value2 = doWordSearch("04-word-search-t2.txt", word_to_search, word_directions, True)

Expected = 25
print("Total result: ", value1)
print("Total result 2: ", value2)
assert value1 == Expected, "Not expected result."


print("%%% Unit 1 %%%")
word_directions = [[1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0]]
word_to_search = "XMAS"
value1, _ = doWordSearch("04-word-search-p1.txt", word_to_search, word_directions)

Expected = 2654
print("Total result: ", value1)
assert value1 == Expected, "Not expected result."


print("%%% Unit 2 %%%")
word_directions = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
word_to_search = "MAS"
value1, value2 = doWordSearch("04-word-search-p1.txt", word_to_search, word_directions)

Expected = 5651
print("Total result: ", value1)
print("Total result 2: ", value2)
assert value1 == Expected, "Not expected result."