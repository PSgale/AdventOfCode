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
    99: ('stop', 0)
}


def retrieve_parameters(memory, position, instruction_name, num_params, param_types, phase_params):
    parameter_indices = memory[position: position + num_params]
    stop_index = 0 if instruction_name in ['output_', 'jump_if_true', 'jump_if_false'] else 1
    for i in range(len(parameter_indices) - stop_index):
        if param_types[-i - 1] == '0':
            parameter_indices[i] = memory[parameter_indices[i]]

    # Add additional parameter
    if instruction_name in ['input_']:
        parameter_indices.append(phase_params.pop())

    return parameter_indices

