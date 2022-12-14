import math
import random

def is_overlapping(x1, x2, y1, y2, x3, x4, y3, y4):
    right_x = min(x2, x4)
    left_x = max(x1, x3)
    top_y = min(y2, y4)
    bot_y = max(y1, y3)

    return left_x <= right_x or top_y <= bot_y

def area(x1, x2, y1, y2):
    return abs(x1-x2)*abs(y1-y2)


def generate4():
    first = random.randint(1, 1000)
    second = random.randint(1, 1000)
    third = random.randint(1, 1000)
    fourth = random.randint(1, 1000)
    return [min(first, second), max(first, second), min(third, fourth), max(third, fourth)]

def find(curr, left, our_squares, total_area):
    if left == 0 and total_area == 0:
        return True
    if curr == len(T):
        return False

    square = T[curr]

    print(type(square))
    print(type(our_squares))
    print(our_squares + square)
    print(square[0])

    if len(our_squares) > 0:
        for sq in our_squares:
            print(type(sq), sq)
            if is_overlapping(sq[0], sq[1], sq[2], sq[3], square[0], square[1], square[2], square[3]):
                return False

    if find(curr + 1, left, our_squares, total_area):
        return True
    elif find(curr + 1, left - 1, our_squares + square, total_area - area(square[0], square[1], square[2], square[3])):
        return True
    return False
        

N = 10
T = [None] * N

for i in range(N):
    T[i] = generate4()

print(T)
print([] + [0])
print(find(0, 13, [], 2012))


