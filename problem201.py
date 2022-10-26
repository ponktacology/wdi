import string

"""Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16"""

digs = string.digits.upper() + string.ascii_letters.upper()
number = 127684356141578287465
base = 16

def change(n, k):
    result = []
    while n > 0:
        result.append(digs[n % k])
        n //= k
    result.reverse()
    return result

if __name__ == "__main__":
    print("".join(change(number, base)))


