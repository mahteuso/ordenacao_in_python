# Ordenação por meio do algoritmo Insertion Sort
import random
import time

l = list(range(21))
random.shuffle(l)
print(l)

def insertion_sort(l):
    n = len(l)
    for i in range(1, n):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l
inicial = time.time()
print(insertion_sort(l))
final = time.time()

total = (final - inicial)*1000
print(f'tempo total: {total}ms')