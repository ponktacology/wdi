"""Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego"""

target = 9 

a = 0
b = 1

while a * b < target:
    a, b = b, a +b
    if a * b == target:
        print(True)
        exit()
print(False)

