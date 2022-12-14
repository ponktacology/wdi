tab = [1, 1, 1, 1, 1, 1, 1, 1, 1]

def licz(n):
    if n == 0:
        return tab[0]
    sum = licz(n - 1)
    return sum + licz(n-2)

print(licz(len(tab) - 1))
