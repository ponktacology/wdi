"""Napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb."""

def gcd(a, b):
    if b <= 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
  return a * b / gcd(a, b)

def lcm1(a, b, c):
    commonDiv = gcd(a, b)
    lcm3 = a*b/commonDiv
    commonDiv = gcd(c, lcm3)
    lcm3 = lcm3*c/commonDiv
    return lcm3

def lcm2(a, b, c):
    lcmA = lcm(a, b)
    lcmB = lcm(c, lcmA)
    return lcmB
    

if __name__ == "__main__":
    print(lcm1(36, 92, 1200))
    print(lcm2(36, 92, 1200))
