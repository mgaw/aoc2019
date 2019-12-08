import sys
from itertools import permutations
from dataclasses import dataclass
from typing import List, Iterable
from collections import deque

def debug(*args):
    if False:
        print(*args)

@dataclass
class Process:
    program: List[int]
    ip: int # instruction pointer
    inputs: deque

def get_operation(p):
    opcode = p.program[p.ip] % 100
    return operations[opcode]

def is_position_mode(value, one_based_param_index):
    return value // (10 * 10 ** one_based_param_index) % 10 == 0

def resolve_param(p, one_based_param_index):
    if is_position_mode(p.program[p.ip], one_based_param_index):
        address = p.program[p.ip + one_based_param_index]
        debug('resolve_param', one_based_param_index, 'position mode', '=>', p.program[address])
    else:
        address = p.ip + one_based_param_index
        debug('resolve_param', one_based_param_index, 'immediate mode', '=>', p.program[address])
    return p.program[address]

def jump(p, address):
    p.ip = address

def advance(p, increment):
    p.ip += increment

def add(p):
    left_value = resolve_param(p, 1)
    right_value = resolve_param(p, 2)
    out_address = p.program[p.ip + 3]
    debug(out_address, '=', left_value, '+', right_value)
    p.program[out_address] = left_value + right_value
    advance(p, 4)

def multiply(p):
    left_value = resolve_param(p, 1)
    right_value = resolve_param(p, 2)
    out_address = program[p.ip + 3]
    debug(out_address, '=', left_value, '*', right_value)
    p.program[out_address] = left_value * right_value
    advance(p, 4)

def input(p):
    address = p.program[p.ip + 1]
    input = p.inputs.popleft()
    debug('using input', input)
    p.program[address] = input
    advance(p, 2)

def output(p):
    value = resolve_param(p, 1)
    advance(p, 2)
    debug('output', value)
    return value

def jump_if_true(p):
    first_value = resolve_param(p, 1)
    if first_value != 0:
        second_value = resolve_param(p, 2)
        jump(p, second_value)
    else:
        advance(p, 3)

def jump_if_false(p):
    first_value = resolve_param(p, 1)
    if first_value == 0:
        second_value = resolve_param(p, 2)
        jump(p, second_value)
    else:
        advance(p, 3)

def less_than(p):
    first_value = resolve_param(p, 1)
    second_value = resolve_param(p, 2)
    out_address = p.program[p.ip + 3]
    if first_value < second_value:
        p.program[out_address] = 1
    else:
        p.program[out_address] = 0
    advance(p, 4)

def equals(p):
    first_value = resolve_param(p, 1)
    second_value = resolve_param(p, 2)
    out_address = p.program[p.ip + 3]
    if first_value == second_value:
        p.program[out_address] = 1
    else:
        p.program[out_address] = 0
    advance(p, 4)

class Halt(Exception):
    pass

def halt(_p):
    raise Halt()

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

def get_next_output(p):
    output = None
    while output is None:
        debug('\nip', p.ip, ':', p.program[p.ip:p.ip + 4])
        output = get_operation(p)(p)
        debug(p.program)
    return output

program = [int(token) for token in next(sys.stdin).split(',')]

max_thrust = 0

for phase_settings in permutations(range(5, 10)):
    debug(phase_settings)
    thrust = 0
    last_e_thrust = 0
    amp_index = 0
    amps = [
        Process(program.copy(), 0, deque([phase_settings[i]]))
        for i in range(5)
    ]
    while True:
        amp = amps[amp_index]
        amp.inputs.append(thrust)
        try:
            debug('\n\namp', amp_index, 'inputs', amp.inputs)
            debug(amp.program)
            thrust = get_next_output(amp)
            debug('thrust', thrust)
        except Halt:
            break
        if amp_index == 4:
            last_e_thrust = thrust  # might not be necessary
            amp_index = 0
        else:
            amp_index += 1
    debug('last_e_thrust:', last_e_thrust)
    if last_e_thrust > max_thrust:
        max_thrust = last_e_thrust

print(max_thrust)
