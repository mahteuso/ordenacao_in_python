"""Estudando o algoritmo de ordenação Bubble sort"""

import random
import time

l = list(range(20))
random.shuffle(l)
print(l)

def booble_sort(l):

    tam = (len(l) - 1)
    while tam > 0:
        i = 0
        while i < tam:
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
            i += 1
        tam -= 1
    return l
antes = time.time()
print(booble_sort(l))
depois = time.time()
total = (depois - antes)*1000
print(f'tempo total: {total}ms')



