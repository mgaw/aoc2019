import sys

def fuel(mass):
    if mass == 0:
        return 0

    fuel_mass = max(int(mass / 3) - 2, 0)
    return fuel_mass + fuel(fuel_mass)

print(sum(fuel(int(line)) for line in sys.stdin))
