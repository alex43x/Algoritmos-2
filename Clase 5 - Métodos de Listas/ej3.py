#Teniendo una lista L de N números y un valor X, se pide eliminar de la lista todas las apariciones del valor.

N=int(input("Ingrese longitud de n:"))
X=int(input("Ingrese valor de x:"))

L=[]

for i in range (N):
    L.append(int(input("Ingrese un valor para la matriz")))

print(L)
while X in L:
    L.remove(X)
    
print(L)
