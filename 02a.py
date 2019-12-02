import sys

program = [int(token) for token in next(sys.stdin).split(',')]
program[1] = 12
program[2] = 2
print(program)

counter = 0

while True:
    opcode = program[counter]
    if opcode == 99:
        break
    if opcode == 1:
        print(counter, ':', opcode, f'program[{program[counter + 3]}] = {program[program[counter + 1]]} + {program[program[counter + 2]]}')
        program[program[counter + 3]] = program[program[counter + 1]] + program[program[counter + 2]]
    if opcode == 2:
        program[program[counter + 3]] = program[program[counter + 1]] * program[program[counter + 2]]
    counter += 4
    print(program)

print(program[0])
