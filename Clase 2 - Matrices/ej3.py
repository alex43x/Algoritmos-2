#Escribir un programa para determinar cual es el cuadro de 2 x 2 elementos que posee la mayor suma en una matriz dada.

from matrices import *

m=int(input("Ingrese cantidad de filas: "))
n=int(input("Ingrese cantidad de columnas: "))

a=creamat(m,n)

for i in range(m):
    for j in range(n):
        a[i][j]=int(input("Ingrese un valor: "))
        
print("Matriz")
for i in range(m):
    print(a[i])
  
sum=0
aux_sum=0  
for i in range(m-1):
    for j in range(n-1):
        sum+=a[i][j]+a[i+1][j]+a[i][j+1]+a[i+1][j+1]
        if aux_sum<sum:
            aux_sum=sum
        sum=0

print("La mayor suma es: ",aux_sum)        
    
        