import math
import array as arr

from instructions import opcode_to_instruction, retrieve_parameters


# Function to read memory
def load_memory(file):
    with open('../data/' + file, 'r') as f:
        memory = [int(i) for i in f.readline().split(',')]
    return memory


# Function to execute program
def execute_program(memory):
    output = []
    i = 0  # position
    while True:
        opcode = ('00000' + str(memory[i]))
        params_types = opcode[:-2]
        instruction, num_params = opcode_to_instruction.get(int(opcode[-2:]))
        if not instruction:
            raise Exception("Unknown opcode. Something went wrong.")
        elif instruction == 'stop':
            print('Command: [' + str(memory[i]) + '] OptCode: ' + opcode[-2:] + ' (' + str(instruction) + ')')
            break
        i += 1
        # parameter_indices = memory[i: i + num_params]
        parameters = retrieve_parameters(memory, i, num_params, params_types)
        print('Command: ' + str(memory[i-1: i + num_params]) + ' OptCode: ' + opcode[-2:] + ' (' + instruction.__name__ + ') Parameters: ' + str(parameters))
        rez = instruction(memory, *parameters)
        if instruction.__name__[0:5] == 'jump_' and rez:
            i = rez
            print('Jump to: ' + str(rez) + ' Next OptCode: ' + ('00000' + str(memory[i])))
        else:
            if rez:
                output.append(rez)
            i += num_params
    return memory, output


# Start program


print("%%% Test 1 %%%")
memory = load_memory("fix_gravity_assyst_t1.txt")
memory, _ = execute_program(memory)

expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
assert memory[0] == expected[0], "Not expected result."


print("%%% Test 2 %%%")
memory = load_memory("fix_gravity_assyst.txt")
# Fix memory
memory[1] = 12
memory[2] = 2
memory, _ = execute_program(memory)

assert memory[0] == 3765464, "Not expected result."


print("%%% Test 3 %%%")
memory = load_memory("incode_computer_t1.txt")
memory, output = execute_program(memory)

print('Entered number: ' + str(output[0]))


print("%%% Test 4 %%%")
memory = load_memory("incode_computer_t2.txt")
memory, output = execute_program(memory)

assert memory[4] == 99, "Not expected result."


print("%%% Test 5 %%%")
memory = load_memory("incode_computer_t3.txt")
memory, output = execute_program(memory)

print(memory)
assert memory[4] == 99, "Not expected result."


print("%%% Test 6 %%%")
memory = load_memory("incode_computer_t4.txt")
memory, output = execute_program(memory)

print(output)
# assert memory[4] == 99, "Not expected result."


print("%%% RUN %%%")
1.
memory = load_memory("incode_computer.txt")
_, output = execute_program(memory)

# Result
print("Test Results : " + str(output))
assert output[-1] == 7692125, "Not expected result."

2.
memory = load_memory("incode_computer2.txt")
_, output = execute_program(memory)

# Result
print("Test Results : " + str(output))
# assert output[-1] == 7692125, "Not expected result."