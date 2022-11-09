"""Dana jest N-elementowa tablica t zawierająca liczby naturalne mniejsze od 1000. Proszę na-
pisać funkcję, która zwraca długość najdłuższego, spójnego fragmentu tablicy, dla którego w iloczynie jego ele-
mentów każdy czynniki pierwszy występuje co najwyżej raz. Na przykład dla tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22]
wynikiem jest wartość 5."""
import math

def consistent(T):
    longest = 0
    curr_length = 0
    digits = [0] * 1000
    for i in T:
        good = True
        for j in range(2, int(math.ceil(math.sqrt(i))) + 1):
            if i % j == 0:
                if digits[j] != 0:
                    good = False
                    break
                else:
                    digits[j] = 1
        if longest < curr_length:
            longest = curr_length
        if not good:
            curr_length = 0
            digits = [0] * 1000
        else:
            curr_length += 1
    return longest

t=[2,23,33,35,7,4,6,7,5,11,13,22]
print(consistent(t))


