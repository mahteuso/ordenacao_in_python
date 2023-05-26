import random

l = list(range(21))
random.shuffle(l)
print(l)

# Ordenação por meio do Bubble Sort

def bubble_sort(l):

    comp = (len(l) - 1)
    while comp > 0:
        i = 0
        while i < comp:
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]

            i += 1
        comp -= 1
    return l

# print(bubble_sort(l))

# Ordenação por meio do Selection Sort

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

#print(selection_sort(l))


