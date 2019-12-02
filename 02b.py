import sys

input_program = [int(token) for token in next(sys.stdin).split(',')]

def result(noun, verb):
    program = input_program.copy()
    program[1] = noun
    program[2] = verb

    counter = 0
    while True:
        opcode = program[counter]
        if opcode == 99:
            break
        if opcode == 1:
            program[program[counter + 3]] = program[program[counter + 1]] + program[program[counter + 2]]
        if opcode == 2:
            program[program[counter + 3]] = program[program[counter + 1]] * program[program[counter + 2]]
        counter += 4

    return program[0]

def find(res):
    for noun in range(100):
        for verb in range(100):
            if res == result(noun, verb):
                return noun * 100 + verb

print(find(19690720))
