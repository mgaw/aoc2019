import sys
from collections import defaultdict

ns = [int(n) for n in next(sys.stdin).strip()]
print(ns)

i = 0
x = 0
y = 0
z = 0
image = {}

for n in ns:
    image[(x, y, z)] = n
    x += 1
    if x > 24:
        x = 0
        y += 1
        if y > 5:
            y = 0
            z += 1

for y in range(6):
    for x in range(25):
        for z in range(100):
            if image[(x, y, z)] == 0:
                print('X', end='')
                break
            if image[(x, y, z)] == 1:
                print(' ', end='')
                break

    print('')
