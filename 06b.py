import sys
from collections import defaultdict

orbiters = defaultdict(list)

for rel in sys.stdin:
    inner, outer = rel.strip().split(')')
    orbiters[inner].append(outer)

stack = ['COM']
paths = {'COM': []}

while stack:
    planet = stack.pop()
    path = paths[planet]
    for orbiter in orbiters[planet]:
        paths[orbiter] = path + [planet]
        stack.append(orbiter)

you = set(paths['YOU'])
san = set(paths['SAN'])

print(len(you - san) + len(san - you))
