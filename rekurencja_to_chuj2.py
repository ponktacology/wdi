import math
import random

def move(w, k):
    if w == 7 and k == 7:
        return True

    moves = [[1,0], [1, 1,], [0, 1]]  

    for p_move in moves:
        to_w = w + p_move[0]
        to_k = k + p_move[1]

        if to_w > 7 or to_w < 0 or to_k > 7 or to_w < 0:
            continue

        if not can_move(w, k, to_w, to_k):
            continue

        if distance(w, k, 7, 7) < distance(to_w, to_k, 7, 7):
            continue
        
        if(move(to_w, to_k)):
            return True

    return False

def can_move(w, k, to_w, to_k):
    global T
    curr = T[w][k]
    to = T[to_w][to_k]

    first_digit = to // 10**int(math.log10(to))
    last_digit = curr % 10
    
    return first_digit > last_digit


def distance(w, k, to_w, to_k):
    return (w-to_w)**2 + (k-to_k)**2


T = [[i for i in range(9)] for i in range(9)]


while True:
    for i in range(9):
        for j in range(9):
            T[i][j] = random.randint(1, 12000)
    if(move(0, 0)):
        print("FOUND")
        print(T)
        break

