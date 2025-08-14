#14-Escribir un algoritmo para jugar el rompecabezas del 15. El mismo consiste en una matriz de 4 filas y 4 columnas que contiene 15 elementos ocupados con los números del 1 al 15 encontrándose el elemento [4,4] ocupado por un valor nulo especial.

#La característica del valor nulo es que el mismo puede desplazarse dentro de la matriz al intercambiarse con un elemento contiguo que se encuentre en la misma fila o columna. En la medida que este elemento se desplaza por la matriz, se va perdiendo el orden inicial.

#1  2  3  4
#5  6  7  8
#9  10 11 12
#13 14 15 0

#El objetivo del juego consiste en devolver el orden a la matriz, una vez que la misma ha sido desordenada por sucesivos desplazamientos del valor nulo. El algoritmo debe producir una situación de matriz desordenada mediante movimientos aleatorios del valor nulo y permitir luego al jugador la oportunidad de reordenar la matriz mediante una secuencia de movimientos del valor nulo.

from matrices import *
from random import randint

def verificar_matriz(A):
    for i in range(4):
        for j in range(4):
            if i*j!=9 and A[i][j]!=4*i+j+1:
                return 0
    return 1            
    
a=creamat(4,4)

#Creación de la matriz
for i in range(4):
    for j in range(4):
        a[i][j]=4*i+j+1
        
a[3][3]=0

print("Matriz")
imprimat(a)
xn=3
yn=3
axn=3
ayn=3

#Reordamiento de las casillas para preparar el juego
for i in range(20):
    valid=0
    while valid==0:
        valid=1
        rn=randint(1,4)
        if rn==1 and xn!=3:
            xn+=1
        elif rn==2 and yn!=3:
            yn+=1
        elif rn==3 and xn!=0:
            xn-=1   
        elif rn==4 and yn!=0:
            yn-=1          
        else:
            valid=0
    a[axn][ayn],a[xn][yn]=a[xn][yn],a[axn][ayn]
    axn=xn
    ayn=yn
    print("Movimiento")
    imprimat(a)


while verificar_matriz(a)==0:
    print("Matriz")
    imprimat(a)
    valid=0
    while valid==0:
        print("Donde deseas mover? ")
        print("1-Abajo")
        print("2-Derecha")
        print("3-Arriba")
        print("4-Izquierda")
        res=int(input())
        valid=1 
        if res==1 and xn!=3:
            xn+=1
        elif res==2 and yn!=3:
            yn+=1
        elif res==3 and xn!=0:
            xn-=1
        elif res==4 and yn!=0:
            yn-=1
        else:
            valid=0
            print("Posición invalida, intente de nuevo")
            imprimat(a)
    a[axn][ayn],a[xn][yn]=a[xn][yn],a[axn][ayn]
    axn=xn
    ayn=yn
    print("Movimiento")
    imprimat(a)
print("Felicidades, haz terminado el juego")
    