"""Napisać program wczytujący trzy liczby naturalne a,b,n i wypisujący rozwinięcie dziesiętne
ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)"""

a = 256
b = 356
n = 5

print(a//b, ".")

for i in range(n):
    a = a % b * 10
    print(a // b)
