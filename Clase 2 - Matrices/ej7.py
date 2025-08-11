#Dada una matriz A[M,N] y la posición [FILA, COLUMNA] de un elemento de la misma, obtener la matriz B que resulta al eliminar la fila y la columna de ese elemento.

from matrices import *

m=int(input("Ingrese cantidad de filas"))
n=int(input("Ingrese cantidad de columnas"))

A=creamat(m,n)

print("Ingrese datos para la matriz")
leemat(A)

print("Matriz")
imprimat(A)

fila=int(input("Ingrese fila a eliminar"))
columna=int(input("Ingrese columna a eliminar"))

B=creamat(m-1,n-1)
ia=0
for i in range(m-1):   
    ja=0
    if ia==fila:
        ia+=1
    for j in range(n-1):
        if ja==columna:
            ja+=1
        B[i][j]=A[ia][ja]
        ja+=1
    ia+=1
    
print("Matriz recortada")
imprimat(B)
            
        
        