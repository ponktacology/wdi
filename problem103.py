"""Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej
sumie."""

target = 2137
sum = 0
a = 1
b = 1

while sum < target:
    sum = sum + a
    a, b = b, a + b

a = 1
b = 1
while sum > target:
    sum = sum - a
    a, b = b, a + b

print(sum == target)
