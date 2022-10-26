"""Napisać program wyznaczający największy wspólny dzielnik 3 zadanych"""

def gcd(a, b):
    if b <= 0:
        return a
    return gcd(b, a%b)

def gcd3(a, b, c):
    return gcd(a, gcd(b, c))

if __name__ == "__main__":
    assert gcd3(36, 72, 192) == 12
    assert gcd3(512, 256, 1024) == 256
