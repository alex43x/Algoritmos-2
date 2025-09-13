from matrices import *

A=creamat(3,9)
print("Ingrese valores de la boleta")
leemat(A)
banderas=[1,1,1,1]
#Revisión regla 1 y 3
nros=[]
ceros=[0,0,0]
for i in range(3):
    for j in range(9):
        if A[i][j]>=1 and A[i][j]<=89 and A[i][j] not in nros:
            nros.append(A[i][j])
        elif A[i][j]==0:
            ceros[i]+=1
        else:
            banderas=[0,1,1,1]
            
if len(nros)!=15:
    banderas=[0,1,1,1]

for i in range(3):
    if ceros[i]!=4:
        banderas[2]=0
        
#Revisión regla 2
scol=[0,0,0,0,0,0,0,0,0]
for i in range(3):
    for j in range(9):
        if A[i][j]>=1 and A[i][j]<=89:
            scol[j]+=1
            if(i==1 and A[i][j]<A[0][j]) or (i==2 and (A[i][j]<A[0][j] or A[i][j]<A[1][j])):
                banderas[1]=0

for i in range(9):
    if scol[i]==0:
        banderas[1]=0
        
#Revision de la regla 4
li=[1,10,20,30,40,50,60,70,80]
ls=[9,19,29,39,49,59,69,79,89]

for i in range(3):
    for j in range(9):
        if A[i][j]!=0 and (li[j]>A[i][j] or ls[j]<A[i][j]):
            banderas[3]=0
            
#Impresión /Salida
for i in range(4):
    if banderas[i]==0:
        print(f"Regla {i+1} no cumple")
    else:
        print(f"Regla {i+1} cumple")

if 0 in banderas:
    print("Boleta incorrecta")
else:
    print("Boleta correcta")