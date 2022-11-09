"""Dwie liczby naturalne są 4-zgodne, jeżeli po zapisaniu ich w systemie o podstawie 4, zbiory cyfr
występujące w liczbie są identyczne. Na przykład:
1310 = 314 i 2310 = 1134
1810 = 1024 i 3310 = 2014
10710 = 12234 i 5710 = 3214.
Dana jest tablica T[N ] zawierająca N liczb naturalnych. Proszę napisać funkcję, która zwraca
długość najdłuższego podciągu (niekoniecznie spójnego) złożonego z liczb 4-zgodnych."""


def fourth_compatibility(a, b):
   digits = [-1] * 4

   while a > 0:
       digits[a % 4] = 1
       a //= 4

   while b > 0:
       if digits[b % 4] < 0:
           return False
       digits[b % 4] = 0
       b //= 4
   for i in digits:
        if i == 1:
            return False

   return True

T = [1, 2, 3, 4, 5, 6, 13, 23, 99,18, 33, 56, 78, 55, 43, 21, 78, 123, 67889, 107, 57, 69, 2137]
length = 0

for i in range(len(T) - 1):
    a = T[i]
    b = T[i + 1]
    if fourth_compatibility(a, b):
        print(a, b)
        length += 1
print(length)


