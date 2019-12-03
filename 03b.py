import sys
from typing import NamedTuple

class Step(NamedTuple):
    dir: str
    distance: int

one = [Step(step[0], int(step[1:])) for step in next(sys.stdin).split(',')]
two = [Step(step[0], int(step[1:])) for step in next(sys.stdin).split(',')]

def path(steps):
    xy = (0, 0)
    visited = {xy: 0}
    counter = 0

    for step in steps:
        x, y = xy
        if step.dir == 'U':
            walk = [(x, y - i - 1) for i in range(step.distance)]
        if step.dir == 'R':
            walk = [(x + i + 1, y) for i in range(step.distance)]
        if step.dir == 'D':
            walk = [(x, y + i + 1) for i in range(step.distance)]
        if step.dir == 'L':
            walk = [(x - i - 1, y) for i in range(step.distance)]
        xy = walk[-1]
        for pos in walk:
            counter += 1
            if pos not in visited:
                visited[pos] = counter

    return visited

ones = path(one)
twos = path(two)

min_distance = None
for crossing in ones.keys() & twos.keys():
    if crossing == (0, 0):
        continue
    distance = ones[crossing] + twos[crossing]
    if not min_distance or distance < min_distance:
        min_distance = distance

print(min_distance)
