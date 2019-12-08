import sys

def debug(*args):
    if False:
        print(*args)

def get_opcode(program, counter):
    return program[counter] % 100

def add(program, left_address, right_address, out_address):
    debug('add', left_address, right_address, out_address)
    program[out_address] = program[left_address] + program[right_address]
    debug(program)

def multiply(program, left_address, right_address, out_address):
    debug('multiply', left_address, right_address, out_address)
    program[out_address] = program[left_address] * program[right_address]
    debug(program)

def input(program, write_address):
    debug('input', write_address)
    program[write_address] = 1
    debug(program)

def output(program, read_address):
    print(program[read_address])

def halt(_program):
    sys.exit()

# returns operation, read arity, write arity
def operation_and_arities(opcode):
    if opcode == 1:
        return add, 2, 1
    if opcode == 2:
        return multiply, 2, 1
    if opcode == 3:
        return input, 0, 1
    if opcode == 4:
        return output, 1, 0
    if opcode == 99:
        return halt, 0, 0


def is_position_mode(value, one_based_param_index):
    return value // (10 * 10 ** one_based_param_index) % 10 == 0

def get_read_param_address(program, counter, one_based_param_index):
    debug('get_read_param_address', counter, program[counter], one_based_param_index)
    if is_position_mode(program[counter], one_based_param_index):
        debug('position mode.')
        return program[counter + one_based_param_index]
    else:
        debug('immediate mode.')
        return counter + one_based_param_index

program = [int(token) for token in next(sys.stdin).split(',')]
debug(program)
counter = 0  # instruction pointer

while True:
    opcode = get_opcode(program, counter)
    operation, read_arity, write_arity = operation_and_arities(opcode)
    read_params = [get_read_param_address(program, counter, i + 1) for i in range(read_arity)]
    write_params = [program[counter + read_arity + i + 1] for i in range(write_arity)]
    operation(program, *read_params, *write_params)
    counter += 1 + read_arity + write_arity
