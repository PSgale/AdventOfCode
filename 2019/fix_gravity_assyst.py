import math
import array as arr


# Function to read memory
def load_memory(file):
    f = open("data/" + file, "r")
    memory_array = arr.array('i')
    for x in f:
        line_array = arr.array('i', [int(i) for i in x.split(",")])
        for el in line_array:
            memory_array.append(el)

    return memory_array


# Function to execute program
def execute_program(memory):
    position = 0;

    while position < len(memory):
        # Adds together numbers
        if memory[position] == 1:
            memory[memory[position + 3]] = memory[memory[position + 1]] + memory[memory[position + 2]]
            position = position + 4
            continue

        # Multiplies two inputs
        elif memory[position] == 2:
            memory[memory[position + 3]] = memory[memory[position + 1]] * memory[memory[position + 2]]
            position = position + 4
            continue

        # Program is finished
        elif memory[position] == 99:
            break

        # Unknown opcode. Something went wrong.
        else:
            raise Exception("Unknown opcode. Something went wrong.")
            # break

    # Something went wrong.
    if position > len(memory) or memory[position] != 99:
        raise Exception("'Program Is Finished' opcode is missing")
        # return arr.array('i', [32000])

    return memory


# Start program


print("%%% Test 1 %%%")
memory = load_memory("fix_gravity_assyst_t1.txt")
memory = execute_program(memory)

expected = arr.array('i', [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])
print("Memory : " + str(memory))
print("Expected : " + str(expected))

# assert not memory[0] == expected[0], "Not expected result."


print("%%% RUN %%%")
memory = load_memory("fix_gravity_assyst.txt")

# Fix memory
memory[1] = 12
memory[2] = 2

# Execute
memory = execute_program(memory)

# Result
print("Value at position 0 : " + str(memory[0]))
# print("Result : " + str(memory))
