import random

l = list(range(9))
random.shuffle(l)
print(l)

def ordenacao(l):

    n = len(l) - 1
    i = 0
    while i < n:
        menor = i
        j = i + 1
        while j < len(l):
            if l[j] < l[menor]:
                menor = j

            j += 1
        l[i], l[menor] = l[menor], l[i]
        i += 1
    return l


print(ordenacao(l))