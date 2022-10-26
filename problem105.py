"""Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona."""

e = 1E-299
square = 25

a = 1
b = square

while abs(a**2 - square) > e:
    a = (a+b)/2
    b = square / a
    
print(a)
