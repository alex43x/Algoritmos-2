#Depósitos de agua - Matriz

from matrices import *

def hallar_sup(A,i,j):
    sw=0
    sp=1
    mi,mj=i,j
    while sw==0:
        if A[mi+1][mj+1]!=0:
            sw=1
        sp+=1
        mi+=1
        mj+=1
        
    min=A[i][j]
    for x in range(i,mi+1):
        for y in range(j,mj+1):
            if A[x][y]<min and A[x][y]!=0:
                min=A[x][y]
    
    data=[i,j,sp**2, (sp**2)*min] 
    
    res.append(data)
    print(res)
    return data
    
A=[[4,3,2,0,5,6,7,6],
   [4,0,3,0,8,0,0,3],
   [2,6,5,0,7,0,0,4],
   [0,0,0,0,3,4,5,3],
   [0,5,6,4,0,0,0,0],
   [0,3,0,6,0,0,0,0],
   [0,7,6,7,0,0,0,0]]

m=int(input("Ingrese cantidad de filas"))
n=int(input("Ingrese cantidad de columnas"))
res=[]

for i in range (m):
    for j in range (n):
        if A[i][j]!=0 and ((A[i-1][j]==0 and A[i][j-1]==0) or (i==0 and A[i][j-1]==0) or (j==0 and A[i-1][j]==0)):
            hallar_sup(A,i,j)


print("Posición     Superficie      Capacidad")            
for i in range(len(res)):
    print(f"{res[i][0]},{res[i][1]}            {res[i][2]}            {res[i][3]}")



