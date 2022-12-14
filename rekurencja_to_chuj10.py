import math
import random

def move(w, k):
    if w == 4:
        return 0
    if w > 4 or w < 4 or k > 4 or k < 4:
        return float('inf')
    if T[w][k]:
        return float('inf')

    return min(min(move(w+1,k-2), move(w+1,k+2)), min(move(w+2, k + 1), move(w + 1, k + 2))) + 1
