#13-Considerando el problema anterior, encontrar cual es el anillo que tiene mayor suma.

#Calcular la suma de la zona indicada en la figura, siendo datos m, n, p, q y los elementos de la matriz:

from matrices import *

m=int(input("Ingrese nro de filas"))
n=int(input("Ingrese nro de columnas"))


        

A=creamat(m,n)

print("Ingrese datos")
leemat(A)

print("Matriz")
imprimat(A)

sum=0
may=0
for p in range(1,m+1):
    for q in range(1,n+1):
        for i in range(m):
            for j in range(n):
                if ((i==p-1 or i==m-p)and(j>=q-1 and j<=n-q)) or ((j==q-1 or j==n-q)and(i>=p-1 and i<=m-p)):
                    sum+=A[i][j]
        if sum>may:
            may=sum
        sum=0 

print(f"La mayor suma es {may}")