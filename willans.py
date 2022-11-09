import math

def prime(n):
    result = 1
    for i in range(1, pow(2, n) + 1):
            sum = 0
            for j in range(1, i + 1):
              # print(math.floor(pow(math.cos((math.pi * (factorial(j - 1) + 1) / j)), 2)), "dupa")
              try: 
                sum = sum + math.floor(pow(math.cos(math.pi * ((factorial(j - 1) + 1) // j)), 2))
              except Exception as e:
                  print(factorial(j-1) + 1 // j, j)
                  raise e
           # print(result)
            result = result + math.floor(pow((n / sum), 1 / n))
    return result

def factorial(n):
   sum = 1
   for i in range(1, n + 1):
      sum = sum * i
   return sum

if __name__ == "__main__":
    print(prime(25), "prime")

