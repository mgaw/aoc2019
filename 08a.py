import sys
from collections import defaultdict

ns = [int(n) for n in next(sys.stdin).strip()]
print(ns)

i = 0
x = 0
y = 0
z = 0
image = {}

layer_value_count = defaultdict(int)

for n in ns:
    image[(x, y, z)] = n
    layer_value_count[(z, n)] += 1
    x += 1
    if x > 24:
        x = 0
        y += 1
        if y > 5:
            y = 0
            z += 1

print(layer_value_count)

layer = min(range(z), key=lambda a: layer_value_count[(a, 0)])
print(layer)
print(layer_value_count[(layer, 1)] * layer_value_count[(layer, 2)])
