"""Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. Z wartości w obu
tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element (z
tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8. Proszę napisać funkcje generującą
i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. Do funkcji należy przekazać dwie
tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum."""

def decimal_to_base(num, base, leng):
    num_base = [0]*leng

    for i in range(len(num_base)-1, -1, -1):
        num_base[i] = num%base
        num //= base
    
    # print(num_base)
    return num_base
T = [1, 2, 3, 4]

print(decimal_to_base(3**(len(T)), 3, len(T)))
