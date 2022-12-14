import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def rozklad(N, A, B, p):
    if N == 0:
        if gcd(A, B) == 1:
            print(A, B)
            return p + 1
        else:
            return 0
    
    zeros = 10**int(math.log10(N))
    digit = N // zeros

    return rozklad(N % zeros, A * 10 + digit, B, p) + rozklad(N % zeros, A, B * 10 + digit, p)

print(rozklad(21523, 0, 0, 0))

