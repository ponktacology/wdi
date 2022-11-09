"""Napisać program wczytujący dwie liczby naturalne i odpowiadający na pytanie czy są one
zbudowane z takich samych cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001."""

import math

a = 1234
b = 321

def same(a, b):
    digits = [0] * 10
    while a > 0:
        digits[a % 10] = 1
        a //= 10
    while b > 0:
        if digits[b % 10] == 1:
            digits[b % 10] = 0
        else: 
            return False
        b //= 10
    for i in range(digits):
        if i == 1:
            return False
    return True

print(same(a, b))
