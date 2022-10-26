"""Napisać program znajdujący wszystkie liczby N-cyfrowe dla których suma N-tych potęg cyfr
liczby jest równa tej liczbie, np. 153 = 13 + 53 + 33"""

def find(n):
    for i in range(10**(n-1), 10**(n)-1):
        init = i
        sum = 0
        while i > 0:
            sum += (i % 10) ** n
            i = i // 10
        if sum == init:
          print(init)
if __name__ == "__main__":
    find(3)    

