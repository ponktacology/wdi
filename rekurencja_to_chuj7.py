
def count_ones(sub_t):
    count = 0
    for i in sub_t:
        while i > 0:
            if i % 2 == 1:
                count += 1
            i //= 2
    return count

T = [4, 1, 5, 9, 12, 13, 16]

def generate(index, first, second, third):
    global T

    if (first and second and third and (len(first) + len(second) + len(third)) == len(T)) and (count_ones(first) == count_ones(second) == count_ones(third)):
        print(first, second, third, count_ones(first), count_ones(second), count_ones(third))
        return True

    if index == len(T):
        return False

    if generate(index + 1, first + [T[index]], second, third):
        return True
    elif generate(index + 1, first, second + [T[index]], third):
        return True
    elif generate(index + 1, first, second, third + [T[index]]):
        return True
    
    return False

print(generate(0, [], [], []))
