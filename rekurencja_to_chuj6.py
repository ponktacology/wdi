def apply(op, x):
    if op == 'A':
        return x + 3
    elif op == 'B':
        return 2 * x
    else:
        new = 0
        n = 0
        while x > 0:
            digit = x % 10
            if digit % 2 == 0:
                digit += 1
            new += digit * 10**n
            n += 1
            x //= 10
        return new

def transform(x, y, n, op):
    if x == y:
        return 1
    if n == 0:
        return 0
    
    if op == 'A':
        return transform(apply('B', x), y, n - 1, 'B') + transform(apply('C', x), y, n - 1, 'C')
    elif op == 'B':
        return transform(apply('A', x), y, n - 1, 'A') + transform(apply('C', x), y, n - 1, 'C')
    elif op == 'C':
        return transform(apply('A', x), y, n - 1, 'A') + transform(apply('B', x), y, n - 1, 'B')
    else:
        return transform(apply('A', x), y, n - 1, 'A') + transform(apply('B', x), y, n - 1, 'B') + transform(apply('C', x), y, n - 1, 'C')

print(transform(11, 31, 4, ''))
