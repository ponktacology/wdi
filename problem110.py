"""Napisać program wyszukujący liczby doskonałe mniejsze od miliona."""


def divisors(n):
  result = set()
  for i in range(1, n + 1):
    if n % i == 0:
      result.add(i)
  return result

def is_perfect(n):
    divs = divisors(n)
    sum = 0
    for i in divs:
        if i < n:
            sum = sum + i
    return sum == n

if __name__ == "__main__": 
    assert is_perfect(28)
    assert is_perfect(6)
    assert not is_perfect(7)
    assert not is_perfect(19)
