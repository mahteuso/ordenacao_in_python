# Ordenação por meio do algoritmo Shell Sort

import random
import time

l = list(range(100000))
random.shuffle(l)
print(l)

def shell_sort(l):
    meio = (len(l) // 2)
    while meio > 0:
        for i in range(meio, len(l)):
            key = l[i]
            j = i - meio
            while j >= 0 and l[j] > key:
                l[j+meio] = l[j]
                j -= meio
            l[j+meio] = key

        meio = (meio // 2)
    return l
inicio = time.time()
print(shell_sort(l))
fim = time.time()

total = (fim - inicio)
print(f'tempo total: {total}m')