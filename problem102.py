"""Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym
do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku."""

target = 2017
best = (0, target)
for i in range(1, target // 2):
    for j in range(1, target // 2):
        first = i
        second = j
        while first + second < target:
            first, second = second, first + second
            if first + second == target and i + j < best[0] + best[1]:
                  best = (i, j)
print(best)
  
