def add(memory, a, b, c):
    memory[c] = a + b
    return None


def multiply(memory, a, b, c):
    memory[c] = a * b
    return None


def input_(memory, a, in_):
    memory[a] = in_
    # int(input("Enter integer: "))
    return None


def output_(memory, a):
    return a


# Opcode 5 is jump-if-true:
# if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter.
# Otherwise, it does nothing.
def jump_if_true(memory, a, b):
    if a != 0:
        return b
    return None


# Opcode 6 is jump-if-false:
# if the first parameter is zero, it sets the instruction pointer to the value from the second parameter.
# Otherwise, it does nothing.
def jump_if_false(memory, a, b):
    if a == 0:
        return b
    return None


# Opcode 7 is less than:
# if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter.
# Otherwise, it stores 0.
def less_than(memory, a, b, c):
    memory[c] = 1 if a < b else 0
    return None


# Opcode 8 is equals:
# if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter.
# Otherwise, it stores 0.
def equals(memory, a, b, c):
    memory[c] = 1 if a == b else 0
    return None


# Opcode 9 is adjusts the relative base :
# Adjusts the relative base by the value of its only parameter.
# The relative base increases (or decreases, if the value is negative) by the value of the parameter.
def adjust_base(memory, a):
    return a


# opcode -> (function, number of parameters)
opcode_to_instruction = {
    1: (add, 3),
    2: (multiply, 3),
    3: (input_, 1),
    4: (output_, 1),
    5: (jump_if_true, 2),
    6: (jump_if_false, 2),
    7: (less_than, 3),
    8: (equals, 3),
    9: (adjust_base, 1),
    99: ('stop', 0)
}


def retrieve_parameters(memory, position, instruction_name, num_params, param_types, phase_params, relative_base):
    parameter_indices = memory[position: position + num_params]
    stop_index = 0 # if instruction_name in ['output_', 'jump_if_true', 'jump_if_false', 'adjust_base'] else 1
    has_output_param = True if instruction_name in ['add', 'multiply', 'input_', 'less_than', 'equals'] else False
    for i in range(len(parameter_indices) - stop_index):
        param_type = param_types[-i - 1]
        parameter_index = parameter_indices[i]

        # evaluate relative index
        if param_type == '2':
            parameter_index += relative_base

        # access memory at index
        if param_type in ['0', '2']:
            if len(memory) < parameter_index + 1:
                memory = extend_memory(memory, parameter_index)

            # read parameter from memory
            if has_output_param and i == len(parameter_indices) - 1:
                parameter_indices[i] = parameter_index
            else:
                parameter_indices[i] = memory[parameter_index]


    # Add additional parameter
    if instruction_name in ['input_']:
        parameter_indices.append(phase_params.pop())

    # Extend memory if index is above allocated memory.
    # if instruction_name in ['add', 'multiply', 'input_', 'less_than', 'equals']:
    #    if len(memory) < parameter_indices[-1] + 1:
    #        memory = extend_memory(memory, parameter_indices[-1])

    return parameter_indices

### Extend memory till requested index
def extend_memory(memory, extend_to):
    memory.extend([0]*(extend_to - len(memory) + 1))
    return memory

