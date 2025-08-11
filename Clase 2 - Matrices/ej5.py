# Una matriz representa la imagen de una zona del mar donde se encuentra una isla. Cada celda representa un cuadro de 100 por 100 metros de superficie y la isla no toca los bordes de la imagen. Los cuadros con valor 1 representan tierra de la isla y los cuadros con valor cero representan el mar. Escribir un programa que calcule el perímetro y el área de la isla.

from matrices import *

m=int(input("Ingrese cantidad de filas "))
n=int(input("Ingrese cantidad de columnas "))

a=creamat(m,n)
ctie=0
cper=0
print("Ingrese valores para la matriz")
leemat(a)

print("Mapa de la isla")
imprimat(a)

for i in range(m-1):
    for j in range(n-1):
        if a[i][j]==1:
            ctie+=1
        if a[i][j]!=a[i][j+1]:
            cper+=1

for j in range(n-1):
    for i in range(m-1):
        if a[i][j]!= a[i+1][j]:
            cper+=1
        
print("El perimetro de la isla es de ", cper*100," cm")    
print("El area es de ",ctie*(100**2)," cm2")
        
