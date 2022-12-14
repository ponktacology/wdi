T = [[0, 5, 4, 3], [2, 1, 3, 2], [8,2,5,1],[4,3,2,0]]

min_pen = float('inf')

def move(w, k, pen):
    print(w, k, pen)
    global T
    global min_pen
    if (w == 3 and k == 3):
        if min_pen > pen:
                min_pen = pen
        return pen

    moves = [(0, 1), (1, 0)]

    for movement in moves:
        next_w = w + movement[0]
        next_k = k + movement[1]
        print(next_w, next_k)
        if next_w < 3 and next_w > 0 and next_k < 3 and next_k > 0:
            move(next_w, next_k, pen + T[w][k])

    return T[w][k]


print(move(0, 0, 0))
