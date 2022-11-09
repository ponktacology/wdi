import math

T = [1, 2, 3, 4, 5, 30, 7, 8, 9, 123, 157]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: 
            return False
    return True

biggest = 0
biggestIndex = None

for i in range(len(T)):
    sum = 1
    for j in range(i):
        if is_prime(T[j]):
            sum *= T[j]
    if sum == T[i] and biggest < T[i]:
        biggest = T[i]
        biggestIndex = i

print(biggestIndex)


