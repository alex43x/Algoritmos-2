#Teniendo las matrices A[m,n] y B[p,q], almacenar en la lista V todos los elementos diferentes que existen en ambas matrices.

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
M=[]

sw=0
for i in range(m):
    for j in range(n):
        for k in range(p):
            for l in range(q):
                if A[i][j]==B[k][l]:
                    M.append(A[i][j])

i=0       
while i!=len(M):
    for j in range(len(M)-i-1):
        if M[i]==M[j]:
            M.pop(j)
    i+=1
print("Comunes")
print(M)

V=[]
for i in range(m):
    for j in range(n):
        if A[i][j] not in M:
            V.append(A[i][j])

for i in range(p):
    for j in range(q):
        if B[i][j] not in M:
            V.append(B[i][j])
            
print("No comunes")
print(V)