"""Estudando o algoritmo de ordenação Selection sort"""
import random

l = list(range(20))
random.shuffle(l)
print(l)

def selection_sort(l):

    for i in range(len(l) - 1):
        menor = i
        j = i + 1

        while j < len(l):
            if l[menor] > l[j]:
                menor = j
            j += 1

        if menor != i:
            l[menor], l[i] = l[i], l[menor]

    return l

print(selection_sort(l))