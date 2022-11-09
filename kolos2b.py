""" Rotacja 1234 o 1 -> 4123
o 2 -> 3412
o 3 -> 2341
o"""
import math

def rotate(n, k):
    digits = int(math.log10(n)) + 1
    k %= digits

    left = n % 10**k
    right = n // 10**k

    return left * 10**(digits - k) + right

print(rotate(1234, 2))

