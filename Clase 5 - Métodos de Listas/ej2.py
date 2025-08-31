#Se cuenta con dos listas de N1 y N2 elementos respectivamente. formar una lista ordenada con todos los elementos que están en una de las listas pero no en la otra.

N1=int(input("Ingrese longitud de n1:"))
N2=int(input("Ingrese longitud de n2:"))

L1=[]
L2=[]
M=[]

for i in range(N1):
    L1.append(int(input("Ingrese un valor para la matriz")))
    
for i in range(N2):
    L2.append(int(input("Ingrese un valor para la matriz")))

for i in range(N1):
    if L1[i] not in L2:
        M.append(L1[i])
    
for j in range(N2):
    if L2[j] not in L1:
        M.append(L2[j])   

M.sort()

print(L1,L2,M) 
            