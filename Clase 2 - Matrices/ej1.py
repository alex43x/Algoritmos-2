#Escribir un programa para hallar la suma de las columnas de una matriz.
from matrices import *

print("Suma de columnas")
m=int(input("Ingrese cantidad de filas "))
n=int(input("Ingrese cantidad de columnas "))

a=creamat(m,n)

sum=[0]*n

for i in range(m):
    for j in range(n):
        a[i][j]=int(input("Ingrese un valor"))
        sum[j]+=a[i][j]
 
print("Matriz")       
for i in range(m):
    print(a[i])  
print("Sumas ",sum)