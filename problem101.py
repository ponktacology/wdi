
"""Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona"""

a = 0
b = 1

while b < 1_000_000:
    print(b)
    a, b = b, a + b

