#Encontrar el máximo elemento de cada fila de una matriz T[m, n]

from matrices import *

m=int(input("Ingrese cantidad de filas "))
n=int(input("Ingrese cantidad de columnas "))

T=creamat(m,n)

max=[0]*m

for i in range(m):
    for j in range(n):
        T[i][j]=int(input("Ingrese un valor: "))
        if T[i][j]>max[i]:
            max[i]=T[i][j]

print("Matriz")

for i in range(m):
    print(T[i])

print("Maximos de filas", max)