import sys
from typing import NamedTuple

class Step(NamedTuple):
    dir: str
    distance: int

one = [Step(step[0], int(step[1:])) for step in next(sys.stdin).split(',')]
two = [Step(step[0], int(step[1:])) for step in next(sys.stdin).split(',')]

def path(steps):
    origin = (0, 0)
    visited = {origin}
    x, y = origin

    for step in steps:
        if step.dir == 'U':
            dx = 0
            dy = -step.distance
        if step.dir == 'R':
            dx = step.distance
            dy = 0
        if step.dir == 'D':
            dx = 0
            dy = step.distance
        if step.dir == 'L':
            dx = -step.distance
            dy = 0
        xmin = min(x, x + dx)
        xmax = max(x, x + dx)
        ymin = min(y, y + dy)
        ymax = max(y, y + dy)
        # probably some duplicates but whatever
        xs = range(xmin, xmax + 1)
        ys = range(ymin, ymax + 1)
        for xx in xs:
            for yy in ys:
                visited.add((xx, yy))
        x += dx
        y += dy
    return visited

ones = path(one)
twos = path(two)

min_distance = None
for crossing in ones & twos:
    if crossing == (0, 0):
        continue
    x, y = crossing
    distance = abs(x) + abs(y)
    if not min_distance or distance < min_distance:
        min_distance = distance

print(min_distance)
