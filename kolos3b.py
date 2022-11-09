"""Dana jest tablica T [N ][N ] wypełniona wartościami 0, 1. Każdy wiersz tablicy traktujemy jako liczbę zapisaną
w systemie dwójkowym o długości N bitów. Stała N jest rzędu 1000. Proszę zaimplementować funkcję
distance(T), która dla takiej tablicy wyznaczy dwa wiersze, dla których różnica zawartych w wierszach
liczb jest największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić odległość pomiędzy
znalezionymi wierszami. Można założyć, że żadne dwa wiersze nie zawierają identycznego ciągu cyfr."""

def distance(T):
    smallest = 2**12
    smallestIndex = 0
    biggest = 0
    biggestIndex = 0
    ops = 0
    for j in range(len(T)):
        row = T[j]
        digit = 0
        for i in range(len(row)):
            digit += row[len(row) - (i + 1)] * 2**i
            ops += 1
        if digit < smallest:
            smallest = digit
            smallestIndex = j
        if digit > biggest:
            biggest = digit
            biggestIndex = j

    print(smallestIndex - biggestIndex)

def distance2(T):
    pos_smallest = 0
    pos_greatest = 0
    smallest = T[0]
    greatest = T[0]
    for pos, row in enumerate(T):
        i = 0
        while i < len(row) and row[i] == smallest[i]:
            i += 1
        print("i", i) 
        if i < len(row) and row[i] == 0:
            print(i, smallest[i], row[i])
            smallest = row
            pos_smallest = pos
    print(pos_smallest)
    
distance2([[0, 1, 1, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1]])




