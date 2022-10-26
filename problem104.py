"""Proszę napisać program obliczający pierwiastek całkowitoliczbowy z liczby naturalnej korzy-
stając z zależności 1 + 3 + 5 + ... = n^2"""

target = 81
sum = 0
for i in range(1, target):
    sum = sum + (2 * i - 1)
    if sum >= target:
        print(i)
        break
