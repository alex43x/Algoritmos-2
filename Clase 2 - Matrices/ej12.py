#Calcular la suma de la zona indicada en la figura, siendo datos m, n, p, q y los elementos de la matriz:

from matrices import *

m=int(input("Ingrese nro de filas"))
n=int(input("Ingrese nro de columnas"))

p=int(input("Ingrese valor de p"))
q=int(input("Ingrese valor de q"))

while p>m:
    p=int(input(f"El valor no debe ser mayor a {m}. Ingrese valor de p"))

while q>n:
    q=int(input(f"El valor no debe ser mayor a {n}. Ingrese valor de q"))
        

A=creamat(m,n)

print("Ingrese datos")
leemat(A)

print("Matriz")
imprimat(A)

sum=0
for i in range(m):
    for j in range(n):
        if ((i==p-1 or i==m-p)and(j>=q-1 and j<=n-q)) or ((j==q-1 or j==n-q)and(i>=p-1 and i<=m-p)):
            sum+=A[i][j]

print(f"La suma es {sum}")