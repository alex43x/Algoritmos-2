#En cierto juego, se cuenta con tablero de 7 filas por 7 columnas en el cual se deben colocar 3 piezas de tamaño 2x2 de tal forma que las mismas no se toquen entre sí, ni por sus lados, ni por sus vértices.

from matrices import *
from random import randint

def check(x,y,A):
    if x==0:
        ix=0
        fx=3
    elif x==5:
        ix=4
        fx=6
    else:
        ix=x-1
        fx=x+3
    
    if y==0:
        iy=0
        fy=3
    elif y==5:
        iy=4
        fy=6
    else:
        iy=y-1
        fy=y+3   
    
    for i in range(ix,fx):
        for j in range(iy,fy):
            print(i,j,x,y)
            if A[i][j]==1:
                return 0
    
    return 1 
        

MAT=creamat(7,7)

for n in range(3):
    vf=0
    while vf==0:
        vf=1
        x=randint(0,5)
        y=randint(0,5)
        if check(x,y,MAT)==0:
            vf=0
    for i in range(0,2):
        for j in range(0,2):
            MAT[x+i][y+j]=1
            
imprimat(MAT)