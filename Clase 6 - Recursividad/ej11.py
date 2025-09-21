#11.Ordenar una lista utilizando el método de intercambio directo.

L=[4,7,3,9,1]
def intercambio_simple(L):
    if len(L)==1:
        return L
    else:
        for i in range(len(L)-1):
            if L[i]>L[i+1]:
                L[i],L[i+1]=L[i+1],L[i]
        return intercambio_simple(L[:len(L)-1])+[L[len(L)-1]]

print(intercambio_simple(L))