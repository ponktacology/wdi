"""Napisać program wypisujący podzielniki liczby."""

def divisors(n):
  result = set()
  for i in range(1, n + 1):
    if n % i == 0:
      result.add(i)
  return result 

if __name__ == "__main__":
    assert divisors(9) == {1, 3, 9}
    assert divisors(12) == {1, 2, 3, 4, 6, 12}
