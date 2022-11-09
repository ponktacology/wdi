"""Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Erato-
stenesa"""

N = 100000000
A = [True] * N

for i in range(2, int(N**(1/2)) + 1):
   n = i
   if A[i]:
     i += i
     while i < N:
        A[i] = False
        i += n

for i in range(len(A) - 2):
    print(i + 2, A[2:][i])
    


