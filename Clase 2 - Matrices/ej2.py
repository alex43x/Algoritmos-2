#Escribir un programa para calcular la suma de las diagonales de una matriz cuadrada de N filas y N columnas.

from matrices import *

N=int(input("Ingrese dimension de la matriz"))

A=creamat(N,N)
sump=0
sums=0
for i in range(N):
    for j in range(N):
        A[i][j]=int(input("Ingrese un valor: "))
        if i+j==N-1:
            sums+=A[i][j]
        if i==j:
            sump+=A[i][j]
            
print("Matriz")
for i in range(N):
    print(A[i])
    
print("Suma diagonal principal: ",sump)
print("Suma diagonal secundaria: ",sums)
