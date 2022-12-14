import math

def build(A, B, N, power):
    if A == 0 and B == 1:
        return
    if (A == 0 and B == 0):
        if not is_prime(N):
            global lista
            lista = lista + [N]
            return
    if B > 0:
        build(A, B-1, N, power + 1)
    if A > 0:
        build(A - 1, B, N + pow(2, power), power + 1)

def is_prime(N):
    if N <= 3:
        return True
    for i in range(2, math.isqrt(N) + 1):
        if N % i == 0:
            return False
    return True

lista = []
build(2, 3, 0, 0)
print(len(lista))
