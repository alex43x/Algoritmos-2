#Para almacenar una serie de “p” números se utiliza la matriz “MAT” de “n” filas y 2 columnas. Cada fila está compuesta de la siguiente manera: la primera columna contiene un número de la serie y la segunda el número de fila en la cual se encuentra el siguiente valor de la serie en orden ascendente.

from matrices import *

MAT=[[5,4],[9,5],[6,2],[2,6],[16,0],[4,3],[0,0],[0,0]]
m=0
srt=[]

def getlisted(MAT):
    srt=[]
    p=MAT[0][0]
    for i in range(1,p+1):
        srt.append(MAT[i][0])
    
    return srt

def buscar(num):
    srt=[]
    srt=getlisted(MAT)
    if num not in srt:
        return 0
    m=min(srt)
    im=srt.index(m)
    return srt.index(num)+2

def agregar(num):
    MAT[0][0]+=1
    p=MAT[0][0]
    MAT[p][0]=num
    
    list=getlisted(MAT)
    srt=list.copy()
    srt.sort()
    
    m=min(srt)
    im=list.index(m)+2
    MAT[0][1]=im
    mx=max(srt)
    for i in range(1,p+1):
        if MAT[i][0]==mx:
            MAT[i][1]=0
        else:
            MAT[i][1]=list.index(srt[(srt.index(MAT[i][0]))+1])+2
            
    return MAT
    
def eliminar(num):
    MAT[0][0]-=1
    p=MAT[0][0]
    
    for i in range(1,p+2):
        if num == MAT[i][0]:
            MAT.pop(i)
    MAT.append([0,0])
    
    
    
    
    list=getlisted(MAT)
    srt=list.copy()
    srt.sort()
    
    m=min(srt)
    im=list.index(m)+2
    MAT[0][1]=im
    mx=max(srt)
    for i in range(1,p+1):
        if MAT[i][0]==mx:
            MAT[i][1]=0
        else:
            MAT[i][1]=list.index(srt[(srt.index(MAT[i][0]))+1])+2
            
    return MAT
    
          
a=agregar(7)
    
print(a)
b=eliminar(4)
print(b)