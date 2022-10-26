import math

"""Napisać program sprawdzający czy zadana liczba jest pierwsza."""

def is_prime(target):
    for i in range(2, math.ceil(math.sqrt(target)) + 1):
      if target % i == 0:
          return False
    return True

if __name__ == "__main__":
    assert is_prime(3)
    assert is_prime(17)
    assert not is_prime(25)
    assert not is_prime(4)

