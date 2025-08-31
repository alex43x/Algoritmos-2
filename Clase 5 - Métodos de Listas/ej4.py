#Procesar las listas L1 de N1 elementos y L2 de N2 elementos para formar la lista L3 que tenga todos los valores comunes a L1 y L2 ordenados ascendentemente. En L3 no deben existir valores repetidos.

N1=int(input("Ingrese longitud de n1:"))
N2=int(input("Ingrese longitud de n2:"))

L1=[]
L2=[]
L3=[]

for i in range(N1):
    L1.append(int(input("Ingrese un valor para la matriz")))
    
for i in range(N2):
    L2.append(int(input("Ingrese un valor para la matriz")))

for i in range(N1):
    if L1[i] in L2 and L1[i] not in L3:
        L3.append(L1[i])
    
for j in range(N2):
    if L2[j] in L1 and L2[j] not in L3:
        L3.append(L2[j])   

L3.sort()

print(L1,L2,L3) 