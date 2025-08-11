#En una matriz G [m,n] encontrar los elementos que son mínimos de su fila y máximos de su columna.

from matrices import *

m=int(input("Ingrese cantidad de filas "))
n=int(input("Ingrese cantidad de columnas "))

G=creamat(m,n)

print("Ingrese valores para la matriz")
leemat(G)

print("Matriz")
imprimat(G)

minf=[999]*m
minc=[999]*n

for i in range(m):
    for j in range(n):
        if G[i][j]<minf[i]:
            minf[i]=G[i][j]
        if G[i][j]<minc[j]:
            minc[j]=G[i][j]

print("Minimos por fila ",minf)
print("Minimos por columna ",minc)