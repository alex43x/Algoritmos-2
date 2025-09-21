#Calcular la suma de los elementos de una lista.

L=[1,2,3,4,5,6,7,8,9]

def suma_lista(L):
    N=len(L)
    if N==1:
        sl=L[0]
    else:
        sl=suma_lista(L[0:N-1])+L[N-1]
    return sl  
      
print(suma_lista(L))
        
        