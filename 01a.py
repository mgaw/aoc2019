import sys

def fuel(mass):
    return max(int(mass / 3) - 2, 0)

print(sum(fuel(int(line)) for line in sys.stdin))
