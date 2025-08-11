#Los datos del censo de población se almacenan en una matriz CENSO [ m , n ], donde cada elemento representa la población de una manzana [m y n son pares]. Se pide formar una nueva matriz RESUMEN donde cada elemento represente la población de un cuadro de 2 * 2 manzanas de la matriz CENSO.

from matrices import *

m=int(input("Ingrese cantidad de filas"))
n=int(input("Ingrese cantidad de columnas"))

while m%2!=0:
    m=int(input("El nro de filas debe ser par. Ingrese cantidad de filas"))
    
while n%2!=0:
    n=int(input("El nro de columnas debe ser par. Ingrese cantidad de columnas"))

CENSO=creamat(m,n)
RESUMEN=creamat(int(m/2),int(n/2))

print("Ingrese datos del censo")
leemat(CENSO)

print("Censo")
imprimat(CENSO)

sum=0
for i in range(int(m/2)):
    for j in range(int(n/2)):
        
        for ii in range(2):
            for jj in range(2):
                RESUMEN[i][j]+=CENSO[i*2+ii][j*2+jj]
                
print("Resumen")
imprimat(RESUMEN)
        


