import random

l = list(range(21))
random.shuffle(l)
print(l)

def selection_sort(l):
    n = len(l)


    for i in range(n - 1):
        menor = i
        j = i + 1
        while j < n:
            if l[j] < l[menor]:
                menor = j
            j += 1
        l[i], l[menor] = l[menor], l[i]

    return l


print(selection_sort(l))

