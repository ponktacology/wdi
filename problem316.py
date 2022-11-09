"""Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwraca-
jącą wartość typu bool oznaczającą, czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie
jeden element największy (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej
wartości)."""

def check(T):
    smallest, biggest = 99999, 0
    smallest_repeated, biggest_repeated = False, False
    for i in T:
        if i < smallest:
            smallest = i
            smallest_repeated = False
        elif i == smallest:
            smallest_repeated = True

        if i > biggest:
            biggest = i
            biggest_repeated = False
        elif i == biggest:
            biggest_repeated = True
    return not (smallest_repeated or biggest_repeated)

print(check([1, 2, 3, 4, 5, 6, 7, 8, -1,  124, 69, 36]))


