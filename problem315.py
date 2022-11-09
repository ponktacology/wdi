"""Dana jest duża tablica t. Proszę napisać funkcję, która zwraca informację czy w tablicy
zachodzi następujący warunek: „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są
liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def is_complex(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        print(n % i, i, n)
        if n % i == 0:
            return True
    return False


def check(T):
    found_prime = False
    fib_a, fib_b = 1, 1
    for i in range(len(T)):
        if fib_a == i:
            if not is_complex(T[i]):
                return False
        elif not found_prime:
            if is_prime(T[i]):
                found_prime = True
        fib_a, fib_b = fib_b, fib_a + fib_b
    return found_prime

T = [4,45,27,6,44,98,10]
print(check(T))
