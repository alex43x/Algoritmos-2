#Se cuenta con una lista V de N números enteros sin valores repetidos (N>1000). Se requiere escribir la función armamat que reciba dicha lista y utilice 9 elementos distintos de V para formar una matriz de 3 filas y 3 columnas, en la cual todas las filas y columnas sumen exactamente la misma cantidad.

from random import sample
from matrices import *


def check(M):
    s=sum(M[0])
    if s!=sum(M[1]): return False
    if s!=sum(M[2]): return False
    
    if M[0][0]+M[1][0]+M[2][0]!=s: return False
    if M[0][1]+M[1][1]+M[2][1]!=s: return False
    if M[0][2]+M[1][2]+M[2][2]!=s: return False
    
    return True
    
    
def armamat(M,V,inten=10):
    t=0
    vf=0
    while t<inten and vf==0:
        muestra=sample(V,9)
        M=[muestra[0:3],muestra[3:6],muestra[6:9]]
        if check(M)==True:
            vf=1
            return M
        else:
            M=[[0,0,0],[0,0,0],[0,0,0]]
        t+=1
    return M

M=creamat(3,3)
V = sample(range(1, 1000), 999)    
M=armamat(M,V,1000000)    
imprimat(M)