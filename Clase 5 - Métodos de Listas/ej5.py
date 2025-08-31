#Solicitar una lista L de N elementos y luego desplazar cada elemento P lugares a la izquierda de su posición actual, cuando un valor sale de la lista por la izquierda, vuelve a ingresar por la derecha de la misma.

N=int(input("Ingrese longitud de n:"))
P=int(input("Ingrese longitud de P:"))

L=[]

A=[0]*N

for i in range(N):
    L.append(int(input("Ingrese un valor para la lista")))
   
   
print(L) 
for i in range(N):
    A[i]=L[i-P]
    
print(A)

