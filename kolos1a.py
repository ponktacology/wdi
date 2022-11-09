"""„Obcięcie” liczby naturalnej polega na usunięciu z niej M początkowych i N końcowych cyfr, gdzie
M, N ⩾ 0. Proszę napisać funkcję, która dla danej liczby naturalnej K zwraca największą liczbę
pierwszą o różnych cyfrach jaką można uzyskać z obcięcia liczby K albo 0, gdy taka liczba nie
istnieje. Na przykład dla liczby 1202742516 spośród obciętych liczb pierwszych: 2, 5, 7, 251, 2027
liczbą spełniającą warunek jest liczba 251."""

import math

K = 1202742516
length = int(math.log10(K)) + 1
digits = [0] * length

def cut(k, m, n):
    while n > 0 and k > 0:
        k //= 10
        n -= 1
    while m > 0 and k > 0:
        kLen = int(math.log10(k))
        k %= 10**kLen
        m -= 1
    return k

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
                   if n % i == 0:
                      return False
    return True

def is_repetetive(n):
    chars = [0] * 9
    while n > 0:
        if chars[n % 10] > 0:
            return True
        chars[n % 10] += 1
        n //= 10
    return False

biggest = 0
for i in range(length - 1):
    for j in range(length - 1):
        digit = cut(K, i, j)
        if digit > 1 and is_prime(digit) and not is_repetetive(digit):
                   if digit > biggest:
                      biggest = digit
print(biggest)
