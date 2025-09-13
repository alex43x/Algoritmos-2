#Dado un valor entero N, se requiere crear una matriz cuadrada MAT [ N, N ] y poblarla con valores aleatorios enteros y distintos entre sí, para luego procesarla de tal forma que las filas y columnas terminen ordenadas ascendentemente de izquierda a derecha y de arriba hacia abajo respectivamente (ver ejemplo en problema anterior).

from random import sample

from matrices import *

N=int(input("Ingrese valor de N: "))

MAT=creamat(N,N)

muestra=sample(range(1,1000),N*N)
muestra.sort()

for i in range(N):
    MAT[i]=muestra[i*N:(i+1)*N]
print(muestra)
imprimat(MAT)