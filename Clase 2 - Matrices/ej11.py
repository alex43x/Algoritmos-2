#11-Ordenar la matriz A[m,n]

from matrices import *

m=int(input("Ingrese cantidad de filas"))
n=int(input("Ingrese cantidad de columnas"))


A=creamat(m,n)
print("Ingrese datos para la matriz")
leemat(A)
print("Matriz")
imprimat(A)

V=[]

for i in range(m):
    for j in range(n):
        V.append(A[i][j])
        
for i in range(len(V)-1):
    for j in range(len(V)-i-1):
        if V[j]>V[j+1]:
            V[j],V[j+1]=V[j+1],V[j]
        
for j in range(m):
    for i in range(n):
        A[i][j]=V[j*m+i]
print(V)
imprimat(A)
