import sys
from collections import defaultdict

orbiters = defaultdict(list)

for rel in sys.stdin:
    inner, outer = rel.strip().split(')')
    orbiters[inner].append(outer)

#print(orbiters)

stack = ['COM']
counts = {'COM': 0}

while stack:
    planet = stack.pop()
    count = counts[planet]
    for orbiter in orbiters[planet]:
        counts[orbiter] = count + 1
        stack.append(orbiter)

print(sum(counts.values()))
