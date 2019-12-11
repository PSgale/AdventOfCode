from instructions import opcode_to_instruction, retrieve_parameters


# Function to read memory
def load_memory(file):
    with open('../data/' + file, 'r') as f:
        memory = [int(i) for i in f.readline().split(',')]
    return memory


# Function to execute program
def execute_program(memory, phase_params, i=0):
    output = []
    status = []
    # i = 0  # position as parameter
    while True:
        opcode = ('00000' + str(memory[i]))
        params_types = opcode[:-2]
        instruction, num_params = opcode_to_instruction.get(int(opcode[-2:]))
        if not instruction:
            raise Exception("Unknown opcode. Something went wrong.")
        elif instruction == 'stop':
            # print('At: ' + str(i) + ' Command: [' + str(memory[i]) + '] OptCode: ' + opcode[-2:] + ' (' + str(instruction) + ')')
            status = [0]
            break
        elif instruction.__name__ == 'input_' and len(phase_params) == 0:
            status = [1, i]  # Pause with freeze step
            break
        i += 1
        parameters = retrieve_parameters(memory, i, instruction.__name__, num_params, params_types, phase_params)
        # print('At: ' + str(i - 1) + ' Command: ' + str(memory[i-1: i + num_params]) + ' OptCode: ' + opcode[-2:] + ' (' + instruction.__name__ + ') Parameters: ' + str(parameters))
        rez = instruction(memory, *parameters)
        if instruction.__name__[0:5] == 'jump_' and rez:
            i = rez
            # print('Jump to: ' + str(rez) + ' Next OptCode: ' + ('00000' + str(memory[i])))
        else:
            if not (rez is None):
                output.append(rez)
            i += num_params
    return memory, output, status


def run_circuit(memory, phase_settings):
    phase_params = [[0], [0], [0], [0], [0]]
    memory_copy = [memory[:], memory[:], memory[:], memory[:], memory[:]]
    status = [[1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]

    cycle = 1
    while any(item[0] > 0 for item in status):
        # 5 amplifiers: A to E
        for i in range(5):
            if status[i][0] == 1:
                # print('Iteration: ' + str(cycle) + '. Amplifier: ' + str(i + 1))
                #print(memory_copy[i])
                if cycle == 1:
                    phase_params[i].append(phase_settings[i])
                memory_copy[i], rez, status[i] = execute_program(memory_copy[i], phase_params[i], status[i][1])
                #print(memory_copy[i])
                result = rez[0]
                if i == 4:
                    phase_params[0] = rez
                else:
                    phase_params[i+1] = rez
        cycle += 1
    return result


# An integer from 0 to 4
# Each integer is used exactly once
def check_phase_settings(phase_settings):
    digits = sorted(phase_settings)
    if any(x < 5 for x in digits):
        return False
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            return False
    return True


def search_best_order(memory):
    output_max = 1
    best_settings = [0, 0, 0, 0, 0]
    for i in range(50000, 99999):
        Phase_Settings = [int(x) for x in list(('0000' + str(i))[-5:])]

        if check_phase_settings(Phase_Settings):
            output = run_circuit(memory, Phase_Settings)
            if output > output_max:
                output_max = output
                best_settings = Phase_Settings
    return output_max, best_settings



# Start program



print("%%% Test 1 %%%")
Memory = load_memory("amplification_circuit2_t1.txt")
Phase_Settings = [9, 8, 7, 6, 5]
Output = run_circuit(Memory, Phase_Settings)

Expected = 139629729
assert Output == Expected, "Not expected result."



print("%%% Test 2 %%%")
Memory = load_memory("amplification_circuit2_t1.txt")
Output_Max, Best_Settings = search_best_order(Memory)

Expected = 139629729
assert Output_Max == Expected, "Not expected result."



print("%%% Test 3 %%%")
Memory = load_memory("amplification_circuit2_t2.txt")
Output_Max, Best_Settings = search_best_order(Memory)

Expected = 18216
assert Output_Max == Expected, "Not expected result."


print("%%% RUN %%%")
# 2.
Memory = load_memory("amplification_circuit2.txt")
Output_Max, Best_Settings = search_best_order(Memory)

print(Output_Max)
print(Best_Settings)



# Result
# print("Test Results : " + str(output))
# assert output[-1] == 7692125, "Not expected result."


