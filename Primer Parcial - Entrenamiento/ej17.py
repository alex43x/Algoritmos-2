#Como parte de un proyecto de programación se requiere construir el procedimiento “ordecol”, capaz de transformar una matriz MAT(M,N), proveída por el usuario, de tal modo que sus columnas queden ordenadas ascendentemente de izquierda a derecha conforme a la suma de cada columna.

from matrices import *

M=int(input("Ingrese valor de M: "))
N=int(input("Ingrese valor de N: "))

MAT=creamat(M,N)

leemat(MAT)

sum=[0]*N

for i in range(M):
    for j in range(N):
        sum[j]+=MAT[i][j]
        
sortsum=sum.copy()
sortsum.sort()

imprimat(MAT)
print(sum,sortsum)

CMAT=creamat(M,N)

for i in range(N):
    for j in range(M):
        CMAT[j][i]=MAT[j][sum.index(sortsum[i])]
    
imprimat(CMAT)
MAT=CMAT.copy()
