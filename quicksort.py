def quicksort(a, start, end):
    if end <= start:
        return
    mid = len(a) // 2
    pivot = a[mid]
    i = start
    j = end
    while i <= j:
      while a[i] < pivot:
        i += 1
      while a[j] > pivot:
        j -= 1
      a[i], a[j] = a[j], a[i]
    if j > start:
        quicksort(a, start, j)
    if i < end:
        quicksort(a, i, end)
a = [9, 6, 3, 2, 1, 4, 5, 8, 7, 0]
quicksort(a, 0, len(a) - 1)
print(a)
