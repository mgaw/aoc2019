import sys

def debug(*args):
    if False:
        print(*args)

instruction_pointer = 0  # short: ip
def jump(address):
    global instruction_pointer
    instruction_pointer = address

def add(program, ip):
    left_value = resolve_param(program, ip, 1)
    right_value = resolve_param(program, ip, 2)
    out_address = program[ip + 3]
    program[out_address] = left_value + right_value
    jump(ip + 4)

def multiply(program, ip):
    left_value = resolve_param(program, ip, 1)
    right_value = resolve_param(program, ip, 2)
    out_address = program[ip + 3]
    program[out_address] = left_value * right_value
    jump(ip + 4)

def input(program, ip):
    address = program[ip + 1]
    program[address] = 5
    jump(ip + 2)

def output(program, ip):
    address = program[ip + 1]
    print(program[address])
    jump(ip + 2)

def jump_if_true(program, ip):
    first_value = resolve_param(program, ip, 1)
    if first_value != 0:
        second_value = resolve_param(program, ip, 2)
        jump(second_value)
    else:
        jump(ip + 3)

def jump_if_false(program, ip):
    first_value = resolve_param(program, ip, 1)
    if first_value == 0:
        second_value = resolve_param(program, ip, 2)
        jump(second_value)
    else:
        jump(ip + 3)

def less_than(program, ip):
    first_value = resolve_param(program, ip, 1)
    second_value = resolve_param(program, ip, 2)
    out_address = program[ip + 3]
    if first_value < second_value:
        program[out_address] = 1
    else:
        program[out_address] = 0
    jump(ip + 4)

def equals(program, ip):
    first_value = resolve_param(program, ip, 1)
    second_value = resolve_param(program, ip, 2)
    out_address = program[ip + 3]
    if first_value == second_value:
        program[out_address] = 1
    else:
        program[out_address] = 0
    jump(ip + 4)

def halt(_program, ip):
    sys.exit()

operations = {
    1: add,
    2: multiply,
    3: input,
    4: output,
    5: jump_if_true,
    6: jump_if_false,
    7: less_than,
    8: equals,
    99: halt,
}

def operation(program, ip):
    opcode = program[ip] % 100
    return operations[opcode]

def is_position_mode(value, one_based_param_index):
    return value // (10 * 10 ** one_based_param_index) % 10 == 0

def resolve_param(program, ip, one_based_param_index):
    debug('resolve_param', ip, program[ip], one_based_param_index)
    if is_position_mode(program[ip], one_based_param_index):
        debug('position mode.')
        address = program[ip + one_based_param_index]
    else:
        debug('immediate mode.')
        address = ip + one_based_param_index
    return program[address]

program = [int(token) for token in next(sys.stdin).split(',')]
debug(program)

while True:
    debug('ip', instruction_pointer, ':', program[instruction_pointer:instruction_pointer + 4])
    operation(program, instruction_pointer)(program, instruction_pointer)
