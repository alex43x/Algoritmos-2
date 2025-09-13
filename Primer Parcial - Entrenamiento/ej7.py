#Escribir un algoritmo en Python que reciba la matriz y el valor de P y luego busque e imprima la ubicación de las dos zonas buscadas. Suponga que el problema siempre tiene una solución.

from matrices import *

m=int(input("Ingrese cantidad de filas"))
n=int(input("Ingrese cantidad de columnas"))
P=int(input("Ingrese el valor de p"))
A=creamat(m,n)
leemat(A)

sum=0
max1=[11,0,0]
max2=[11,0,0]
#Busca el mas acercado
for i in range(m-1):
    for j in range(n-1):
       sum=A[i][j]+A[i+1][j]+A[i][j+1]+A[i+1][j+1]
       print(max1[0],abs(P-sum))
       if abs(P-sum)<=10 and max1[0]>abs(P-sum):
           max1=[abs(P-sum),i,j]
           
imprimat(A)    

#Busca el segundo mas acercado que no choque con el primero

for i in range(m-1):
    for j in range(n-1):
        sum=A[i][j]+A[i+1][j]+A[i][j+1]+A[i+1][j+1]
        print(max1[0],abs(P-sum)) 
        if abs(P-sum)<=10 and max2[0]>abs(P-sum) and ((i<max1[1]-2 or i>max1[1]+2)or(j<max1[2]-2 or j>max1[2]+2)):
           max2=[abs(P-sum),i,j]
           
print (max1)
print (max2)
           
            


