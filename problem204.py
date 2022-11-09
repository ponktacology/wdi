"""Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! + 1/1! +
1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000)."""


n = 2
b = 1
a = 1
digits = [0] * (n + 1)
dupa = True
while digits[n] == 0:
  a = a * b
  b = b + 1 
  digit = 1
  print(digits)
  for i in range(n):
       digit = digit % a * 10
       if(digit % a == 0): break
       digits[i] = digits[i] + (digit // a)
print(digits)
