import math

def apply(x, operation):
    if operation == 'A':
        if x >= 10:
            first = x % 10
            second = (x // 10) % 10
            return ((x // 100) * 100) + (10 * first) + second
        return x
    elif operation == 'B':
        return x * 3
    else:
        if x >= 10:
            return x % 10**int(math.log10(x))
        return x

def transform(x, y, ops, left):
    if x == y:
        return "".join(ops)
    if left == 0:
        return ""

    ops[7 - left] = 'A'
    transform(apply(x, 'A'), y, ops, left - 1)
    ops[7 - left] = 'B'
    transform(apply(x, 'B'), y, ops, left - 1)
    ops[7 - left] = 'C'
    transform(apply(x, 'C'), y, ops, left - 1)

print(transform(6, 3, [0] * 7, 7))
    
