#10.Ordenar una lista utilizando el método de selección directa.
L=[4,7,3,9,1]
def selection_sort(L):
    if len(L)==1:
        return L
    else:
        L.remove(min(L))
        return [min(L)]+selection_sort(L)

print(selection_sort(L))
