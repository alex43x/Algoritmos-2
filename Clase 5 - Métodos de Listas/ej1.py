#Se cuenta con una lista L1 de N números, sin elementos repetidos. Se solicita obtener otra lista L2, indicando la posición que ocuparía cada elemento de L1 si la misma se ordenara ascendentemente.

N=int(input("Ingrese longitud de n:"))
L1=[]
L2=[0]*N
A1=[]
for i in range (N):
    L1.append(int(input("Ingrese un valor para la matriz")))
    
A1=L1.copy()
A1.sort()
print(L1,A1)

for i in range(N):
    for j in range(N):
        if A1[i]==L1[j]:
            L2[j]=i+1
            
print(L2)