"""SUDOKU TAA(2017)"""
from matrices import *
MAT=[
    [5,3,2,6,0,1],
    [0,4,6,0,2,5],
    [6,0,1,0,3,0],
    [3,2,4,0,5,6],
    [4,1,5,2,6,3],
    [2,0,3,5,1,4]
]

ff=[[1,2,3,4,5,6] for _ in range(6)]
fc=[[1,2,3,4,5,6] for _ in range(6)]
print(ff)
print(fc)

#Hallar faltantes
for i in range(6):
    for j in range(6):
        if MAT[i][j]!=0 :
            if MAT[i][j] in ff[i]:
                ff[i].remove(MAT[i][j])
            if MAT[i][j] in fc[j]:
                fc[j].remove(MAT[i][j])

print(ff)
print(fc)
imprimat(MAT)
                
#Relleno
for i in range(6):
    for j in range(6):
        if MAT[i][j]==0:
            comunes=[x for x in ff[i] if x in fc[j]]
            if len(comunes)==1:
                MAT[i][j]=comunes[0]
                ff[i].remove(comunes[0])
                fc[j].remove(comunes[0])

print(ff)
print(fc)
imprimat(MAT)
