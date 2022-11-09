"""Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje."""

def find_longest(T):
     balance = 0
     curr_length = 0
     max_length = 0
     for i in range(1, len(T)):
         if T[i - 1] >= T[i]:
             balance = 0
             curr_length = 0
         else:
             balance += T[i] - i
             print("b:", balance, "cl:", curr_length, "t[i]", T[i], "t[i -= 1]", T[i-1])
             if balance <= 0:
                 print("extend")
                 curr_length += 1
                 if curr_length > max_length:
                     max_length = curr_length
             elif balance > 0:
                 print("reset")
                 balance = 0
                 curr_length = 0

     print(max_length)

find_longest([-1, 0, 3, 4])





         
