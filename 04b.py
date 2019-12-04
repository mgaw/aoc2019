import sys

def has_real_double(digits):
    count = 1
    digit = None
    for d in digits:
        if d == digit:
            count += 1
        else:
            if count == 2:
                return True
            count = 1
            digit = d
    if count == 2:
        return True

    return False

def is_monotonically_increasing(digits):
    prev = 0
    for d in digits:
        if d < prev:
            return False
        prev = d
    return True

def get_digits(n):
    # not the fastest way to do this...
    # < and == would even work on strings
    return [int(d) for d in str(n)]

counter = 0
low, high = next(sys.stdin).split('-')

for n in range(int(low), int(high) + 1):
    digits = get_digits(n)
    if has_real_double(digits) and is_monotonically_increasing(digits):
        counter += 1

print(counter)
