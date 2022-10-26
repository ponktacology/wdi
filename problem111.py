"""Napisać wyszukujący liczby zaprzyjaźnione mniejsze od miliona"""

def is_befriended(a, b):
    if a == b or a % b == 0:
        return False
    
    sum = 0
    for i in range(1, a):
        if a % i == 0:
           sum = sum + i
           if sum > b:
               return False
    
    if sum != b:
        return False
    
    sum = 0
    for i in range(1, b):
        if b % i == 0:
          sum = sum + i
          if sum > a:
              return False
    
    if sum != a:
        return False
    
    return True

if __name__ == "__main__":
    assert is_befriended(220, 284)
    for i in range(1, 10000):
        for j in range(1, 10000):
            if is_befriended(i, j):
                print(i, j)

