"""Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! + 1/1! +
1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000)."""


def euler(n):
    ops = 0
    divisor = 1
    a = 1
    digits = [0] * n
    digits[0] = 1
    while True:
        divisor *= a
        a += 1

        onlyZeros = True
        divident = 1
        for i in range(n):
            ops += 1
            if divident // divisor > 0:
                onlyZeros = False
            digits[i] += divident // divisor
            if digits[i] > 9:
                digits[i] %= 10
                digits[i - 1] += 1
            if divident % divisor == 0:
                break
            divident = (divident % divisor) * 10
        if onlyZeros:
            break
    print(ops)
    return digits

print(euler(10))



    


