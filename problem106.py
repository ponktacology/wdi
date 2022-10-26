"""Proszę napisać program rozwiązujący równanie xx = 2020 metodą bisekcji."""

target = 2020

def f(x):
    return x**x - target

e = 1E-12
a = 0
b = 100

x = (a+b)/2

while abs(f(x)) > e:
    x = (a+b)/2
    if f(a)*f(x) < 0:
        b = x
    if f(b)*f(x) < 0:
        a = x
print((a+b)/2) 

