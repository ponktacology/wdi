import math

"""Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym."""

def digit(num, pos):
   return int(num // 10**pos) % 10

def palindrome(n):
    size = int(math.log10(n)) + 1
    for i in range(size):
        if digit(n, i) != digit(n, size - (1 + i)):
            return False
    return True

def size(n): return int(math.log10(n)) + 1

if __name__ == "__main__":
    assert palindrome(6996)
    assert palindrome(123456789987654321)
    assert not palindrome(1488)
    assert not palindrome(2137)
