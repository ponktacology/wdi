"""Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończo-
nych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów."""

nums = [95, 6, 12, 7, 1, 2, 3, 123, 8, 78, 6, 7, 12, 73, 83, 93, 1234]

# while (a = int(input(""))) != 0:
 #   nums.append(a)

# bubble sort xd
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[j] < nums[i]:
            nums[j], nums[i] = nums[i], nums[j]

print(nums[10])


