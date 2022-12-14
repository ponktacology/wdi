import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def divide(N, seg):
    if N == 0:
        if is_prime(len(seg)):
            for i in seg:
                if not is_prime(i):
                    return False
            print(seg)
            return True
        return False

    zeros = 10 ** int(math.log10(N))
    digit = N // zeros
    
    if divide(N % zeros, seg + [digit]):
       return True
    else:
        for i in range(len(seg)):
            seg[i] = seg[i] * 10 + digit
            if divide(N % zeros, seg):
                return True
            seg[i] = seg[i] // 10
    return False

print(divide(23672, []))
