"""Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
podciągu lub wartość 0 jeżeli taki podciąg nie istnieje"""

def check(T):
    start = -1
    length = 0
    for i in range(len(T)):
        print(T[i])
        if T[i] % 2 != 0:
            length += 1
            print("l", length)
        else:
            start = i + 1
            print("r", start)
            length = 0 
    print(start, start + length)



def is_palindrome(A):
    for i in range(len(A) // 2):
        if A[i] != A[len(A) - i - 1]:
            return False
    return True

print(is_palindrome([1, 2, 3,4, 2, 1]))
print(check([1, 2, 3, 4, 5, 6, 7, 3, 3, 3, 3, 3, 3, 3]))

