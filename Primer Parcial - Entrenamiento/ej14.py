#Se requiere escribir la función BUSMAT, que reciba como parámetros la matriz MAT y un número Z y retorne la posición (fila y columna) dentro de la matriz en la cual se encuentra el valor Z. Si la matriz no contiene el valor Z, la función deberá retornar fila=0 columna=0. La función BUSMAT deberá realizar su trabajo de la manera más eficiente posible. 

from matrices import *
N=6
MAT=[[8, 11, 13, 22, 49, 55],
     [10, 18, 30, 44, 60, 64],
     [15, 27, 43, 58, 78, 81],
     [21, 39, 53, 72, 86, 90],
     [32, 52, 65, 83, 87, 92],
     [50, 63, 79, 85, 94, 96]]
Z=79

def BUSMAT(MAT, Z):
    x=0
    y=N-1
    while x<N and y>=0:
        if MAT[x][y]==Z:
            return [x,y]
        elif MAT[x][y]>Z:
            y-=1
        else:
            x+=1
    return [0,0]
            
            
c=BUSMAT(MAT,Z)
print(c)