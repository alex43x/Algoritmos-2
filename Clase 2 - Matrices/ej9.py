#Teniendo las matrices A[m,n] y B[p,q], almacenar en la lista V todos los elementos comunes de ambas matrices.

from matrices import *

m=int(input("Ingrese cantidad de filas"))
n=int(input("Ingrese cantidad de columnas"))

p=int(input("Ingrese cantidad de filas"))
q=int(input("Ingrese cantidad de columnas"))

A=creamat(m,n)
B=creamat(p,q)

leemat(A)
leemat(B)

imprimat(A)

imprimat(B)
V=[]

for i in range(m):
    for j in range(n):
        for k in range(p):
            for l in range(q):
                if A[i][j]==B[k][l]:
                    V.append(A[i][j])
        
while i!=len(V):
    for j in range(len(V)-i):
        if V[i]==V[j]:
            V.pop(j)
    i+=1
print("Comunes")
print(V)